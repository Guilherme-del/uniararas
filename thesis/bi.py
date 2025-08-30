# -*- coding: utf-8 -*-
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ===================== Config fixo =====================
OUT_DIR = "./bi"
os.makedirs(OUT_DIR, exist_ok=True)

# posição/altura da tabela (fixo)
TABLE_Y0 = -0.62   # quão baixo a tabela fica (mais negativo => mais baixo)
TABLE_H  = 0.42    # altura da tabela
BOTTOM0  = 0.60    # margem inferior para caber a tabela

# legenda sempre fora, à direita (fixo)
LEGEND_NCOL = 2  # colunas na legenda

SIZE_ORDER_ALIASES = {
    "small": 1, "medium": 2, "large": 3,
    "pequeno": 1, "medio": 2, "grande": 3
}

COLORS_VIBRANT = [
    "#377EB8", "#E41A1C", "#4DAF4A", "#984EA3", "#FF7F00",
    "#FFFF33", "#A65628", "#F781BF", "#999999", "#66C2A5",
    "#FC8D62", "#8DA0CB", "#E78AC3", "#A6D854",
]

HEADER_SHORT = {
    "c": "C",
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

# ===================== Load & Clean =====================
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
    mean_col = f"{value_prefix}_mean"
    std_col  = f"{value_prefix}_std"
    if (mean_col not in agg_df.columns) or (std_col not in agg_df.columns):
        return None, None

    m = agg_df.pivot_table(index=index_col, columns=column_col, values=mean_col, aggfunc="mean")
    s = agg_df.pivot_table(index=index_col, columns=column_col, values=std_col,  aggfunc="mean")

    m = m.fillna(0.0) if m is not None else pd.DataFrame()
    s = s.fillna(0.0) if s is not None else pd.DataFrame()

    m = ensure_size_index(m)
    s = s.reindex(m.index)
    return m, s

def plot_lines_with_table(mean_df, std_df, title, ylabel, filename):
    if mean_df is None or mean_df.empty:
        return

    x = np.arange(len(mean_df.index))
    base_h = 9 + 0.45 * max(0, len(x) - 1)
    fig_w = 18  # mais largo para caber a legenda do lado de fora
    plt.figure(figsize=(fig_w, base_h))

    # paleta
    colors = {c: COLORS_VIBRANT[i % len(COLORS_VIBRANT)] for i, c in enumerate(mean_df.columns)}

    # linhas + barras de erro
    for col in mean_df.columns:
        y = mean_df[col].values
        yerr = std_df[col].values if (std_df is not None and col in std_df.columns) else None
        plt.errorbar(
            x, y, yerr=yerr, fmt='-o', linewidth=1.8, markersize=5,
            color=colors[col], ecolor=colors[col], capsize=4, label=str(col)
        )

    plt.title(title)
    plt.xlabel("Tamanho do dataset")
    plt.ylabel(ylabel)
    plt.xticks(x, [str(v) for v in mean_df.index])
    plt.grid(True, axis='y', alpha=0.25)

    # ---------- LEGENDA fora (direita) ----------
    plt.legend(ncol=LEGEND_NCOL, title="Séries", loc="upper left",
               bbox_to_anchor=(1.02, 1.0), borderaxespad=0.0)

    # ===== CSV “igual à tabela” =====
    table_df = pd.DataFrame(index=[str(i) for i in mean_df.index])
    for c in mean_df.columns:
        table_df[f"{short_label(c)} – M"]  = np.round(mean_df[c].values, 3)
        table_df[f"{short_label(c)} – DP"] = np.round(std_df[c].values, 3) if std_df is not None else np.nan
    table_df.index.name = "Tamanho"
    table_df.to_csv(os.path.join(OUT_DIR, f"{filename}_tabela.csv"))

    # ===== Tabela embaixo (sem repetir a linguagem: “colspan” simulado) =====
    langs = list(mean_df.columns)
    top = ["Tamanho"]
    for c in langs:
        top += [f"{short_label(c)}", ""]  # nome da linguagem só na 1ª célula do par (M, DP)
    sub = [""] + ["M", "DP"] * len(langs)

    body = []
    for idx in mean_df.index:
        row = [str(idx)]
        for c in langs:
            mval = mean_df.loc[idx, c]
            sval = std_df.loc[idx, c] if std_df is not None else np.nan
            row += [f"{mval:.2f}", ("" if (sval is None or np.isnan(sval)) else f"{sval:.2f}")]
        body.append(row)

    ncols = 1 + 2 * len(langs)
    w0 = 0.16
    w_each = (1.0 - w0) / (ncols - 1)
    colw = [w0] + [w_each] * (ncols - 1)

    tbl = plt.table(
        cellText=[top, sub] + body,
        cellLoc="center",
        colWidths=colw,
        loc="bottom",
        bbox=[0.0, TABLE_Y0, 1.0, TABLE_H],
    )
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(10)
    tbl.scale(1.0, 1.18)

    extra = 0.02 * max(0, len(mean_df.index) - 1)
    plt.subplots_adjust(left=0.08, right=0.98, top=0.88, bottom=BOTTOM0 + extra)

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
    if "linguagem" not in agg_df.columns:
        return
    for lang in sorted(agg_df["linguagem"].unique()):
        sub = agg_df[agg_df["linguagem"] == lang]
        mean_col = f"{value_prefix}_mean"
        std_col  = f"{value_prefix}_std"
        if sub.empty or mean_col not in sub.columns or std_col not in sub.columns:
            continue
        m = sub.pivot_table(index="tamanho", columns="linguagem", values=mean_col, aggfunc="mean")
        s = sub.pivot_table(index="tamanho", columns="linguagem", values=std_col,  aggfunc="mean")
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

print("✅ BI concluído. Saída em:", OUT_DIR)
