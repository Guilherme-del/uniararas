# -*- coding: utf-8 -*-
import os
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

COLORS_VIBRANT = [
    "#377EB8",  # blue
    "#E41A1C",  # red
    "#4DAF4A",  # green
    "#984EA3",  # purple
    "#FF7F00",  # orange
    "#FFFF33",  # yellow
    "#A65628",  # brown
    "#F781BF",  # pink/magenta
    "#999999",  # gray
    "#66C2A5",  # teal
    "#FC8D62",  # salmon
    "#8DA0CB",  # periwinkle
    "#E78AC3",  # rose
    "#A6D854",  # lime
]

HEADER_SHORT = {
    "javascript": "JS",
    "typescript": "TS",
    "csharp": "C#",
    "c#": "C#",
    "cpp": "C++",
    "c++": "C++",
    "golang": "Go",
    "python": "Py",
}

def short_label(lang: str) -> str:
    k = str(lang).strip().lower()
    if k in HEADER_SHORT:
        return HEADER_SHORT[k]
    s = str(lang)
    return s if len(s) <= 9 else s[:9]

def parse_k_suffix(x: str):
    try:
        s = str(x).strip().lower()
        if s.endswith('k'):
            return int(float(s[:-1]) * 1000)
        return int(float(s))
    except Exception:
        return None

def size_sort_key(v):
    n = parse_k_suffix(v)
    if n is not None:
        return (0, n)
    rank = SIZE_ORDER_ALIASES.get(str(v).lower())
    if rank is not None:
        return (1, rank)
    return (2, str(v))

def ensure_size_index(df):
    ordered = sorted(df.index.unique(), key=size_sort_key)
    return df.reindex(ordered)

def savefig(path, tight=False):
    if tight:
        plt.savefig(path, dpi=120, bbox_inches='tight', pad_inches=1.0)
    else:
        plt.tight_layout()
        plt.savefig(path, dpi=120)
    plt.clf()

# ===================== Load & Clean (somente métricas novas) =====================

df = pd.read_json("./resultados/metricas.json")

# mantém só execuções válidas e com tempo > 0
if "exit_code" in df.columns:
    df = df[df["exit_code"] == 0]
if "timeout_s" in df.columns:
    df = df[df["timeout_s"] == 0]
df = df[df["tempo_s"] > 0].copy()

# normalizações de texto
for col in ("linguagem", "tamanho", "classe", "algoritmo"):
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip()
if "algoritmo" in df.columns:
    df["algoritmo_norm"] = df["algoritmo"].str.lower()

# flags de colunas
HAS_CPU_NORM = "cpu_avg_during_norm" in df.columns
HAS_RAM      = "ram_avg_during_mb" in df.columns

# ===================== Agregações base =====================

agg_spec = {"tempo_s": ["mean", "std", "count"]}
if HAS_CPU_NORM:
    agg_spec["cpu_avg_during_norm"] = ["mean", "std", "count"]
if HAS_RAM:
    agg_spec["ram_avg_during_mb"] = ["mean", "std", "count"]

group_cols = [c for c in ["linguagem", "tamanho"] if c in df.columns]
agg = (df.groupby(group_cols, as_index=False).agg(agg_spec))
# achata MultiIndex
agg.columns = ["_".join([c for c in col if c]) if isinstance(col, tuple) else col
               for col in agg.columns.to_list()]
agg.to_csv(os.path.join(OUT_DIR, "resumo_agg.csv"), index=False)

# ===================== Helpers de plot com tabela =====================

def pivot_mean_std(agg_df, value_prefix, index_col="tamanho", column_col="linguagem"):
    m = agg_df.pivot_table(index=index_col, columns=column_col, values=f"{value_prefix}_mean", aggfunc="mean")
    s = agg_df.pivot_table(index=index_col, columns=column_col, values=f"{value_prefix}_std",  aggfunc="mean")
    m = m.fillna(0.0)
    s = s.fillna(0.0)
    m = ensure_size_index(m)
    s = s.reindex(m.index)
    return m, s

def plot_lines_with_table(mean_df, std_df, title, ylabel, filename):
    if mean_df is None or mean_df.empty:
        return
    x = np.arange(len(mean_df.index))
    plt.figure(figsize=(16, 9 + 0.35 * max(0, len(x) - 1)))
    colors = {c: COLORS_VIBRANT[i % len(COLORS_VIBRANT)] for i, c in enumerate(mean_df.columns)}

    for col in mean_df.columns:
        y = mean_df[col].values
        yerr = std_df[col].values if (std_df is not None and col in std_df.columns) else None
        plt.errorbar(x, y, yerr=yerr, fmt='-o', linewidth=1.8, markersize=5,
                     color=colors[col], ecolor=colors[col], capsize=4, label=str(col))

    plt.title(title)
    plt.xlabel("Tamanho do dataset")
    plt.ylabel(ylabel)
    plt.xticks(x, [str(v) for v in mean_df.index])
    plt.grid(True, axis='y', alpha=0.25)
    plt.legend(ncol=2, title="Séries")

    # CSV “igual à tabela”
    table_df = pd.DataFrame(index=[str(i) for i in mean_df.index])
    for c in mean_df.columns:
        table_df[f"{short_label(c)} – M"]  = np.round(mean_df[c].values, 3)
        table_df[f"{short_label(c)} – DP"] = np.round(std_df[c].values, 3) if std_df is not None else np.nan
    table_df.index.name = "Tamanho"
    table_df.to_csv(os.path.join(OUT_DIR, f"{filename}_tabela.csv"))

    # Tabela compacta no gráfico
    top = ["Tamanho"] + [f"{short_label(c)}" for c in mean_df.columns for _ in (0, 1)]
    sub = [""] + ["M", "DP"] * len(mean_df.columns)
    body = []
    for idx in mean_df.index:
        row = [str(idx)]
        for c in mean_df.columns:
            m = mean_df.loc[idx, c]
            s = std_df.loc[idx, c] if std_df is not None else np.nan
            row += [f"{m:.2f}", ("" if (s is None or np.isnan(s)) else f"{s:.2f}")]
        body.append(row)

    ncols = 1 + 2 * len(mean_df.columns)
    w0 = 0.16
    w_each = (1.0 - w0) / (ncols - 1)
    colw = [w0] + [w_each] * (ncols - 1)

    tbl = plt.table(cellText=[top, sub] + body, cellLoc="center",
                    colWidths=colw, loc="bottom",
                    bbox=[0.0, -0.38, 1.0, 0.34])
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(10)
    tbl.scale(1.0, 1.18)

    plt.subplots_adjust(left=0.08, right=0.98, top=0.88, bottom=0.46)
    savefig(os.path.join(OUT_DIR, f"{filename}.png"), tight=True)

# ===================== Gráficos principais (todas as linguagens) =====================

m, s = pivot_mean_std(agg, "tempo_s")
plot_lines_with_table(m, s, "Tempo de Execução × Tamanho (todas as linguagens)", "Tempo (s)", "tempo_vs_tamanho_all")

if HAS_CPU_NORM and "cpu_avg_during_norm_mean" in agg.columns:
    m, s = pivot_mean_std(agg, "cpu_avg_during_norm")
    plot_lines_with_table(m, s, "CPU média normalizada × Tamanho (todas as linguagens)", "CPU média normalizada (%)", "cpu_vs_tamanho_all")

if HAS_RAM and "ram_avg_during_mb_mean" in agg.columns:
    m, s = pivot_mean_std(agg, "ram_avg_during_mb")
    plot_lines_with_table(m, s, "RAM média × Tamanho (todas as linguagens)", "RAM (MB)", "ram_vs_tamanho_all")

# ===================== Por linguagem (arquivos separados) =====================

def plot_per_language(agg_df, value_prefix, title_prefix, ylab, fname_prefix):
    if "linguagem" not in agg_df.columns: return
    for lang in sorted(agg_df["linguagem"].unique()):
        sub = agg_df[agg_df["linguagem"] == lang]
        if sub.empty or f"{value_prefix}_mean" not in sub.columns: 
            continue
        m = sub.pivot_table(index="tamanho", columns="linguagem", values=f"{value_prefix}_mean", aggfunc="mean")
        s = sub.pivot_table(index="tamanho", columns="linguagem", values=f"{value_prefix}_std",  aggfunc="mean")
        m = ensure_size_index(m); s = s.reindex(m.index)
        title = f"{title_prefix} – {lang}"
        fname  = f"{fname_prefix}_{lang}"
        plot_lines_with_table(m, s, title, ylab, fname)

plot_per_language(agg, "tempo_s", "Tempo × Tamanho", "Tempo (s)", "tempo_vs_tamanho")
if HAS_CPU_NORM:
    plot_per_language(agg, "cpu_avg_during_norm", "CPU normalizada × Tamanho", "CPU média normalizada (%)", "cpu_vs_tamanho")
if HAS_RAM:
    plot_per_language(agg, "ram_avg_during_mb", "RAM × Tamanho", "RAM (MB)", "ram_vs_tamanho")

# ===================== Linhas de código =====================

if "linhas_codigo" in df.columns:
    # por linguagem
    loc_lang = df.groupby("linguagem")["linhas_codigo"].mean().sort_values()
    loc_lang.to_csv(os.path.join(OUT_DIR, "linhas_codigo_media_por_linguagem.csv"))
    ax = loc_lang.plot(kind="bar", figsize=(10,6), title="Média de linhas de código por linguagem")
    plt.ylabel("Linhas de código")
    plt.xlabel("Linguagem")
    for cont in ax.containers:
        ax.bar_label(cont, fmt="%.0f", fontsize=8)
    savefig(os.path.join(OUT_DIR, "linhas_codigo_por_linguagem.png"))

    # por linguagem × classe
    if "classe" in df.columns:
        loc_lang_cls = df.groupby(["linguagem","classe"])["linhas_codigo"].mean().unstack().fillna(0)
        loc_lang_cls.to_csv(os.path.join(OUT_DIR, "linhas_codigo_linguagem_classe.csv"))
        ax = loc_lang_cls.plot(kind="bar", figsize=(12,6), title="Média de linhas de código por linguagem e classe")
        plt.ylabel("Linhas de código")
        plt.xlabel("Linguagem")
        plt.xticks(rotation=45)
        for cont in ax.containers:
            ax.bar_label(cont, fmt="%.0f", fontsize=8)
        savefig(os.path.join(OUT_DIR, "linhas_codigo_linguagem_classe.png"))

# ===================== Tempo por classe polinomial =====================

if "classe" in df.columns:
    tempo_classe = df.groupby("classe")["tempo_s"].mean().sort_values()
    tempo_classe.to_csv(os.path.join(OUT_DIR, "tempo_medio_por_classe.csv"))
    ax = tempo_classe.plot(kind="bar", figsize=(8,5), title="Tempo médio por classe de complexidade")
    plt.ylabel("Tempo (s)")
    plt.xlabel("Classe")
    for cont in ax.containers:
        ax.bar_label(cont, fmt="%.3f", fontsize=8)
    savefig(os.path.join(OUT_DIR, "tempo_medio_por_classe.png"))

# ===================== Knapsack (NP-Completo): Exato vs Guloso =====================

if "classe" in df.columns and "algoritmo_norm" in df.columns:
    knap = df[(df["classe"].str.lower() == "np-completo") &
              (df["algoritmo_norm"].isin(["exato", "guloso"]))].copy()
    if not knap.empty and "tamanho" in knap.columns:
        sizes = sorted(knap["tamanho"].unique(), key=size_sort_key)
        focus_sizes = sizes[:2] if len(sizes) >= 2 else sizes
        knap2 = knap[knap["tamanho"].isin(focus_sizes)].copy()

        spec = {"tempo_s": ["mean","std","count"]}
        if HAS_CPU_NORM: spec["cpu_avg_during_norm"] = ["mean","std","count"]
        if HAS_RAM:      spec["ram_avg_during_mb"]   = ["mean","std","count"]

        aggk = (knap2
                .groupby(["linguagem","tamanho","algoritmo_norm"], as_index=False)
                .agg(spec))
        aggk.columns = ["_".join([c for c in col if c]) if isinstance(col, tuple) else col
                        for col in aggk.columns.to_list()]
        aggk.to_csv(os.path.join(OUT_DIR, "knapsack_exato_vs_guloso.csv"), index=False)

        def piv(sub, prefix):
            m = sub.pivot(index="tamanho", columns="algoritmo_norm", values=f"{prefix}_mean").fillna(0)
            s = sub.pivot(index="tamanho", columns="algoritmo_norm", values=f"{prefix}_std").fillna(0)
            m = ensure_size_index(m); s = s.reindex(m.index)
            return m, s

        for lang in sorted(aggk["linguagem"].unique()):
            sub = aggk[aggk["linguagem"] == lang]
            if sub.empty: continue

            m, s = piv(sub, "tempo_s")
            plot_lines_with_table(m, s, f"Knapsack – Tempo – {lang}", "Tempo (s)", f"knapsack_tempo_{lang}")

            if HAS_CPU_NORM and "cpu_avg_during_norm_mean" in sub.columns:
                m, s = piv(sub, "cpu_avg_during_norm")
                plot_lines_with_table(m, s, f"Knapsack – CPU (norm) – {lang}", "CPU média normalizada (%)", f"knapsack_cpu_{lang}")

            if HAS_RAM and "ram_avg_during_mb_mean" in sub.columns:
                m, s = piv(sub, "ram_avg_during_mb")
                plot_lines_with_table(m, s, f"Knapsack – RAM – {lang}", "RAM (MB)", f"knapsack_ram_{lang}")

# ===================== (Opcional) Qualidade de solução =====================
# Requer colunas: 'valor_objetivo', identificação da instância (ex: 'instancia' ou 'dataset_id'),
# e pares exato × guloso na MESMA instância.
if {"valor_objetivo", "algoritmo_norm"}.issubset(df.columns) and \
   ({"instancia"} & set(df.columns) or {"dataset_id"} & set(df.columns)):
    case_col = "instancia" if "instancia" in df.columns else "dataset_id"
    exato = df[(df.get("classe","").str.lower() == "np-completo") &
               (df["algoritmo_norm"] == "exato") &
               df[case_col].notna()][[case_col, "valor_objetivo"]].rename(columns={"valor_objetivo":"valor_otimo"})
    heur = df[(df.get("classe","").str.lower() == "np-completo") &
              (df["algoritmo_norm"] == "guloso") &
              df[case_col].notna()][[case_col, "valor_objetivo", "linguagem", "tamanho"]]
    merged = pd.merge(heur, exato, on=case_col, how="inner")
    if not merged.empty:
        merged["qualidade"] = merged["valor_objetivo"] / merged["valor_otimo"]
        q = merged.groupby(["linguagem","tamanho"])["qualidade"].agg(["mean","std","count"]).reset_index()
        q.to_csv(os.path.join(OUT_DIR, "knapsack_qualidade.csv"), index=False)
        m = q.pivot(index="tamanho", columns="linguagem", values="mean").fillna(np.nan)
        s = q.pivot(index="tamanho", columns="linguagem", values="std").fillna(0.0)
        m = ensure_size_index(m); s = s.reindex(m.index)
        plot_lines_with_table(m, s, "Qualidade da solução (Heurística/Ótimo) – Knapsack", "Razão (↑ melhor)", "knapsack_qualidade")

print("✅ BI concluído. Saída em:", OUT_DIR)
