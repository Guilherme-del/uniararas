import os
import re
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ===================== Config / Helpers =====================

OUT_DIR = "./bi"
os.makedirs(OUT_DIR, exist_ok=True)

SIZE_ORDER_ALIASES = {
    "small": 1, "medium": 2, "large": 3,
    "pequeno": 1, "medio": 2, "grande": 3
}

EXACT_NAMES = {"exato","exact","ótimo","otimo","optimal","dp","backtracking","branch_and_bound","knapsack_exato"}
APPROX_NAMES = {"guloso","greedy","heuristica","heurística","approx","aproximado","knapsack_guloso"}

def parse_k_suffix(x: str):
    """Converte '1k' -> 1000, '10k'->10000; números puros viram int; fallbacks mantêm string."""
    try:
        s = str(x).strip().lower()
        if s.endswith('k'):
            return int(float(s[:-1]) * 1000)
        return int(float(s))
    except Exception:
        return None

def size_sort_key(v):
    """Ordena tamanhos: tenta número; senão usa aliases; senão por string."""
    n = parse_k_suffix(v)
    if n is not None:
        return (0, n)
    rank = SIZE_ORDER_ALIASES.get(str(v).lower())
    if rank is not None:
        return (1, rank)
    return (2, str(v))

def ensure_monotonic_size_index(df):
    """Ordena index de tamanhos em ordem lógica (1k, 10k, 100k / small, medium, large)."""
    ordered = sorted(df.index.unique(), key=size_sort_key)
    return df.reindex(ordered)

def savefig(path):
    plt.tight_layout()
    plt.savefig(path, dpi=120)
    plt.clf()

def plot_error_lines(mean_df: pd.DataFrame, std_df: pd.DataFrame, title: str, ylabel: str, filename: str, xlabel="Tamanho do dataset"):
    """Plota linhas com barras de erro (uma figura por gráfico)."""
    if mean_df.empty:
        return
    mean_df = ensure_monotonic_size_index(mean_df)
    std_df = std_df.reindex(mean_df.index)

    x = np.arange(len(mean_df.index))
    plt.figure(figsize=(10, 6))
    for col in mean_df.columns:
        y = mean_df[col].values
        yerr = std_df[col].values if col in std_df.columns else None
        plt.errorbar(x, y, yerr=yerr, capsize=4, label=str(col))
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.xticks(x, [str(v) for v in mean_df.index], rotation=0)
    plt.legend()
    savefig(os.path.join(OUT_DIR, f"{filename}.png"))

def group_keys(df: pd.DataFrame, base=("linguagem","tamanho")):
    keys = [k for k in base if k in df.columns]
    # Adiciona 'algoritmo' e 'classe' se existirem (úteis p/ fatiar depois)
    for opt in ("algoritmo","classe"):
        if opt in df.columns and opt not in keys:
            keys.append(opt)
    return keys

# ===================== Load & Clean =====================

df = pd.read_json("./resultados/metricas.json")
df = df[df.get("tempo_s", 0) > 0].copy()

# Normaliza alguns nomes (opcional)
if "algoritmo" in df.columns:
    df["algoritmo_norm"] = df["algoritmo"].astype(str).str.strip().str.lower()
else:
    df["algoritmo_norm"] = np.nan

# ===================== Agregações (média, desvio, n) =====================

keys = group_keys(df, base=("linguagem","tamanho"))
metrics = {
    "tempo_s": ["mean","std","count"],
    "cpu_avg_during": ["mean","std","count"] if "cpu_avg_during" in df.columns else [],
    "ram_avg_during_mb": ["mean","std","count"] if "ram_avg_during_mb" in df.columns else [],
}
# Remove métricas ausentes
metrics = {k:v for k,v in metrics.items() if len(v)>0}

agg = df.groupby(keys).agg(metrics)
# Achata MultiIndex de colunas
agg.columns = ["_".join([c for c in tup if c]) for tup in agg.columns.to_flat_index()]
agg = agg.reset_index()
agg.to_csv(os.path.join(OUT_DIR, "resumo_agg.csv"), index=False)

# ===================== Gráficos principais com barras de erro =====================

def pivot_mean_std(agg: pd.DataFrame, value_prefix: str, index_col="tamanho", column_col="linguagem", extra_filters=None):
    sub = agg.copy()
    if extra_filters:
        for k,v in extra_filters.items():
            sub = sub[sub[k]==v]
    m = sub.pivot(index=index_col, columns=column_col, values=f"{value_prefix}_mean")
    s = sub.pivot(index=index_col, columns=column_col, values=f"{value_prefix}_std")
    m = m.fillna(0)
    s = s.fillna(0)
    return m, s

# Tempo vs Tamanho (todas as linguagens)
m, s = pivot_mean_std(agg, "tempo_s", index_col="tamanho", column_col="linguagem")
plot_error_lines(m, s, "Tempo de Execução × Tamanho (todas as linguagens)", "Tempo (s)", "tempo_vs_tamanho_all")

# CPU vs Tamanho (se disponível)
if "cpu_avg_during_mean" in agg.columns:
    m, s = pivot_mean_std(agg, "cpu_avg_during", index_col="tamanho", column_col="linguagem")
    plot_error_lines(m, s, "CPU média × Tamanho (todas as linguagens)", "CPU média (%)", "cpu_vs_tamanho_all")

# RAM vs Tamanho (se disponível)
if "ram_avg_during_mb_mean" in agg.columns:
    m, s = pivot_mean_std(agg, "ram_avg_during_mb", index_col="tamanho", column_col="linguagem")
    plot_error_lines(m, s, "RAM média × Tamanho (todas as linguagens)", "RAM (MB)", "ram_vs_tamanho_all")

# ===================== Gráficos por linguagem/algoritmo (um por arquivo) =====================

def plot_per_group(agg: pd.DataFrame, value_prefix: str, group_col: str, title_prefix: str, fname_prefix: str):
    if group_col not in agg.columns:
        return
    for g in sorted(agg[group_col].dropna().unique()):
        sub = agg[agg[group_col]==g]
        if sub.empty: 
            continue
        m = sub.pivot(index="tamanho", columns="linguagem" if group_col!="linguagem" else "algoritmo" if "algoritmo" in sub.columns else "classe", values=f"{value_prefix}_mean")
        s = sub.pivot(index="tamanho", columns=m.columns.name, values=f"{value_prefix}_std")
        if m is None or m.empty: 
            continue
        title = f"{title_prefix} – {group_col}: {g}"
        fname = f"{fname_prefix}_{group_col}_{str(g)}"
        plot_error_lines(m, s, title, ylabel={"tempo_s":"Tempo (s)","cpu_avg_during":"CPU média (%)","ram_avg_during_mb":"RAM (MB)"}[value_prefix], filename=fname)

# Por linguagem: como RAM e Tempo escalam com tamanho
plot_per_group(agg, "tempo_s", "linguagem", "Tempo × Tamanho", "tempo_vs_tamanho")
if "ram_avg_during_mb_mean" in agg.columns:
    plot_per_group(agg, "ram_avg_during_mb", "linguagem", "RAM × Tamanho", "ram_vs_tamanho")

# ===================== Linhas de código =====================

if "linhas_codigo" in df.columns:
    loc_media = df.groupby("linguagem")["linhas_codigo"].mean().sort_values()
    loc_media.to_csv(os.path.join(OUT_DIR, "tabela_linhas_codigo_media_por_linguagem.csv"))
    ax = loc_media.plot(kind="bar", figsize=(10,6), title="Média de linhas de código por linguagem")
    plt.ylabel("Linhas de código")
    plt.xlabel("Linguagem")
    for c in ax.containers:
        ax.bar_label(c, fmt="%.0f", fontsize=8)
    savefig(os.path.join(OUT_DIR, "linhas_codigo_por_linguagem.png"))

    if "classe" in df.columns:
        loc_lang_cls = df.groupby(["linguagem","classe"])["linhas_codigo"].mean().unstack().fillna(0)
        loc_lang_cls.to_csv(os.path.join(OUT_DIR, "tabela_linhas_codigo_linguagem_classe.csv"))
        ax = loc_lang_cls.plot(kind="bar", figsize=(10,6), title="Média de linhas de código por linguagem e classe")
        plt.ylabel("Linhas de código")
        plt.xlabel("Linguagem")
        plt.xticks(rotation=45)
        for c in ax.containers:
            ax.bar_label(c, fmt="%.0f", fontsize=8)
        savefig(os.path.join(OUT_DIR, "linhas_codigo_linguagem_classe.png"))

# ===================== Knapsack: exato vs guloso (tempo/CPU/RAM) nos menores datasets =====================

def is_knapsack_row(row):
    # tenta identificar knapsack por classe ou campos extras
    if str(row.get("problema","")).lower() == "knapsack":
        return True
    if str(row.get("classe","")).lower() in {"np-completo","np completo","np_completo"}:
        # opcional: se você marcar no JSON um campo problema="knapsack", melhor.
        # Aqui mantemos generoso: muitos dos seus 'np-completo' são Knapsack.
        return True
    return False

if "tamanho" in df.columns:
    knap = df[df.apply(is_knapsack_row, axis=1)].copy()
    if not knap.empty and "algoritmo_norm" in knap.columns:
        # Identifica menores tamanhos (pegar os 2 mais baixos)
        sizes_sorted = sorted(knap["tamanho"].unique(), key=size_sort_key)
        menores = sizes_sorted[:2] if len(sizes_sorted) >= 2 else sizes_sorted
        knap_small = knap[knap["tamanho"].isin(menores)].copy()

        # Marca tipo (exato vs guloso) a partir do nome do algoritmo
        def tipo_alg(s):
            s = str(s).lower()
            if any(name in s for name in EXACT_NAMES):
                return "exato"
            if any(name in s for name in APPROX_NAMES):
                return "guloso"
            return np.nan
        if "algoritmo" in knap_small.columns:
            knap_small["tipo"] = knap_small["algoritmo"].apply(tipo_alg)
        else:
            knap_small["tipo"] = np.nan

        # Se não conseguirmos identificar, não plota
        if knap_small["tipo"].notna().any():
            keys_knap = [k for k in ("linguagem","tamanho","tipo") if k in knap_small.columns]
            agg_knap = knap_small.groupby(keys_knap).agg({
                k: ["mean","std","count"] for k in ["tempo_s"] 
                if k in knap_small.columns
            })
            if "cpu_avg_during" in knap_small.columns:
                agg_c = knap_small.groupby(keys_knap)["cpu_avg_during"].agg(["mean","std","count"])
                agg_knap[("cpu_avg_during","mean")] = agg_c["mean"]
                agg_knap[("cpu_avg_during","std")] = agg_c["std"]
                agg_knap[("cpu_avg_during","count")] = agg_c["count"]
            if "ram_avg_during_mb" in knap_small.columns:
                agg_r = knap_small.groupby(keys_knap)["ram_avg_during_mb"].agg(["mean","std","count"])
                agg_knap[("ram_avg_during_mb","mean")] = agg_r["mean"]
                agg_knap[("ram_avg_during_mb","std")] = agg_r["std"]
                agg_knap[("ram_avg_during_mb","count")] = agg_r["count"]

            agg_knap.columns = ["_".join([c for c in tup if c]) for tup in agg_knap.columns.to_flat_index()]
            agg_knap = agg_knap.reset_index()
            agg_knap.to_csv(os.path.join(OUT_DIR, "knapsack_small_exato_vs_guloso.csv"), index=False)

            # Para cada linguagem, tempo/CPU/RAM vs tamanho comparando exato x guloso
            for lang in sorted(agg_knap["linguagem"].unique()):
                sub = agg_knap[agg_knap["linguagem"]==lang]
                if sub.empty: 
                    continue

                def piv(v):
                    m = sub.pivot(index="tamanho", columns="tipo", values=f"{v}_mean").fillna(0)
                    s = sub.pivot(index="tamanho", columns="tipo", values=f"{v}_std").fillna(0)
                    return m, s

                if "tempo_s_mean" in sub.columns:
                    m,s = piv("tempo_s")
                    plot_error_lines(m, s, f"Knapsack (Exato vs Guloso) – Tempo – {lang}", "Tempo (s)", f"knapsack_tempo_{lang}")

                if "cpu_avg_during_mean" in sub.columns:
                    m,s = piv("cpu_avg_during")
                    plot_error_lines(m, s, f"Knapsack (Exato vs Guloso) – CPU – {lang}", "CPU média (%)", f"knapsack_cpu_{lang}")

                if "ram_avg_during_mb_mean" in sub.columns:
                    m,s = piv("ram_avg_during_mb")
                    plot_error_lines(m, s, f"Knapsack (Exato vs Guloso) – RAM – {lang}", "RAM (MB)", f"knapsack_ram_{lang}")

# ===================== (Opcional) Qualidade da solução da heurística =====================
# Para calcular qualidade, ideal ter:
# - uma coluna identificando a instância/caso (ex: 'instancia' ou 'dataset_id')
# - 'valor_objetivo' (valor obtido) para cada execução
# - para os casos com algoritmo exato, o 'valor_otimo' da MESMA instância
#
# Se você expor isso no JSON, podemos fazer: qualidade = valor_heuristica / valor_otimo

def compute_solution_quality(df_knap: pd.DataFrame):
    cols_case = [c for c in ("instancia","dataset_id","caso_id","arquivo","dataset_nome") if c in df_knap.columns]
    if not cols_case:
        print("[INFO] Para qualidade da solução, adicione uma coluna de identificação de caso (ex: 'instancia').")
        return pd.DataFrame()

    case_col = cols_case[0]

    if not {"valor_objetivo","algoritmo_norm",case_col}.issubset(df_knap.columns):
        print("[INFO] Para qualidade da solução, adicione 'valor_objetivo' (numérico) e 'algoritmo'.")
        return pd.DataFrame()

    exato = df_knap[df_knap["algoritmo_norm"].isin(EXACT_NAMES)][[case_col,"valor_objetivo"]].rename(columns={"valor_objetivo":"valor_otimo"})
    heur = df_knap[df_knap["algoritmo_norm"].isin(APPROX_NAMES)][[case_col,"valor_objetivo","linguagem","tamanho"]]

    merged = pd.merge(heur, exato, on=case_col, how="inner")
    if merged.empty:
        print("[INFO] Não foi possível casar heurística com exato. Verifique 'instancia'/'dataset_id'.")
        return pd.DataFrame()

    merged["qualidade"] = merged["valor_objetivo"] / merged["valor_otimo"]
    # Agrega por linguagem/tamanho para plot
    q = merged.groupby(["linguagem","tamanho"])["qualidade"].agg(["mean","std","count"]).reset_index()
    q.to_csv(os.path.join(OUT_DIR, "knapsack_qualidade.csv"), index=False)

    # Plota qualidade (quanto mais perto de 1.0, melhor)
    m = q.pivot(index="tamanho", columns="linguagem", values="mean").fillna(np.nan)
    s = q.pivot(index="tamanho", columns="linguagem", values="std").fillna(0.0)
    plot_error_lines(m, s, "Qualidade da solução (Heurística/Ótimo) – Knapsack", "Razão (↑ melhor)", "knapsack_qualidade")
    return merged

# Descomente quando tiver 'valor_objetivo' e identificador de instância no JSON:
# if not knap.empty:
#     compute_solution_quality(knap)
