# -*- coding: utf-8 -*-
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ===================== Config fixo =====================
OUT_DIR = "./bi"
os.makedirs(OUT_DIR, exist_ok=True)

# layout de tabela separada
TABLE_FONT_SIZE = 10
TABLE_SCALE_Y = 1.2

# legenda fora, à direita
LEGEND_NCOL = 2

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

GREEDY_ALIASES = {
    "guloso", "greedy",
    "heuristica", "heurístico", "heuristico",
    "aproximacao", "aproximação", "approx", "heuristic"
}

# ===================== Utils =====================
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

# ===== métricas escolhidas =====
HAS_CPU_MAX_NORM = "cpu_max_during_norm" in df.columns
HAS_RAM_PEAK     = "ram_peak_mb" in df.columns

# Fallback automático (se só houver médias)
if (not HAS_CPU_MAX_NORM) and ("cpu_avg_during_norm" in df.columns):
    df["cpu_max_during_norm"] = df["cpu_avg_during_norm"]
    HAS_CPU_MAX_NORM = True
if (not HAS_RAM_PEAK) and ("ram_avg_during_mb" in df.columns):
    df["ram_peak_mb"] = df["ram_avg_during_mb"]
    HAS_RAM_PEAK = True

# ===================== Filtro global (Opção A) =====================
# Excluir COMPLETAMENTE NP-Completo dos gráficos gerais (tempo/cpu/ram)
df_general = df[df["classe"].str.lower() != "np-completo"].copy()

# ===================== Helpers de agregação/plot =====================
def build_agg(dataframe: pd.DataFrame):
    agg_spec = {"tempo_s": ["mean", "std", "count"]}
    if HAS_CPU_MAX_NORM:
        agg_spec["cpu_max_during_norm"] = ["mean", "std", "count"]
    if HAS_RAM_PEAK:
        agg_spec["ram_peak_mb"] = ["mean", "std", "count"]
    group_cols = [c for c in ["linguagem", "tamanho"] if c in dataframe.columns]
    agg_df = (dataframe.groupby(group_cols, as_index=False).agg(agg_spec))
    # achata MultiIndex
    agg_df.columns = ["_".join([c for c in col if c]) if isinstance(col, tuple) else col
                      for col in agg_df.columns.to_list()]
    return agg_df

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

def _table_to_png(mean_df, std_df, filename_base, index_name="Tamanho"):
    """Gera PNG e CSV da tabela separada."""
    # CSV
    table_df = pd.DataFrame(index=[str(i) for i in mean_df.index])
    for c in mean_df.columns:
        table_df[f"{short_label(c)} – M"]  = np.round(mean_df[c].values, 3)
        table_df[f"{short_label(c)} – DP"] = np.round(std_df[c].values, 3) if std_df is not None else np.nan
    table_df.index.name = index_name
    table_df.to_csv(os.path.join(OUT_DIR, f"{filename_base}_tabela.csv"))

    # PNG
    langs = list(mean_df.columns)
    top = [index_name]
    for c in langs:
        top += [f"{short_label(c)}", ""]
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

    fig_w = 12
    fig_h = 2 + 0.3 * max(1, len(body))
    fig_tab, ax_tab = plt.subplots(figsize=(fig_w, fig_h))
    ax_tab.axis("off")

    tbl = ax_tab.table(
        cellText=[top, sub] + body,
        cellLoc="center",
        colWidths=colw,
        loc="center",
    )
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(TABLE_FONT_SIZE)
    tbl.scale(1.0, TABLE_SCALE_Y)

    plt.savefig(os.path.join(OUT_DIR, f"{filename_base}_table.png"),
                dpi=120, bbox_inches="tight")
    plt.close(fig_tab)

def plot_lines_with_table(mean_df, std_df, title, ylabel, filename):
    """Gera gráfico (sem título) e tabela separada (PNG + CSV)."""
    if mean_df is None or mean_df.empty:
        return

    # ---------- gráfico ----------
    x = np.arange(len(mean_df.index))
    fig_w, fig_h = 12, 6
    plt.figure(figsize=(fig_w, fig_h))

    colors = {c: COLORS_VIBRANT[i % len(COLORS_VIBRANT)] for i, c in enumerate(mean_df.columns)}

    for col in mean_df.columns:
        y = mean_df[col].values
        yerr = std_df[col].values if (std_df is not None and col in std_df.columns) else None
        plt.errorbar(
            x, y, yerr=yerr, fmt='-o', linewidth=1.8, markersize=5,
            color=colors[col], ecolor=colors[col], capsize=4, label=str(col)
        )

    # (sem título)
    plt.xlabel("Tamanho do dataset")
    plt.ylabel(ylabel)
    plt.xticks(x, [str(v) for v in mean_df.index])
    plt.grid(True, axis='y', alpha=0.25)
    plt.legend(ncol=LEGEND_NCOL, title="Séries", loc="upper left",
               bbox_to_anchor=(1.02, 1.0), borderaxespad=0.0)

    savefig(os.path.join(OUT_DIR, f"{filename}.png"), tight=True)

    # ---------- tabela separada ----------
    _table_to_png(mean_df, std_df, filename_base=filename, index_name="Tamanho")

# ===================== Agregações (GERAIS, sem NP-Completo) =====================
agg_general = build_agg(df_general)

# 1) TEMPO – geral (sem NP-Completo)
m, s = pivot_mean_std(agg_general, "tempo_s")
plot_lines_with_table(
    m, s,
    "",  # sem título
    "Tempo (s)",
    "tempo_vs_tamanho_all"
)

# 2) CPU MÁXIMA NORMALIZADA – geral (sem NP-Completo)
if HAS_CPU_MAX_NORM and "cpu_max_during_norm_mean" in agg_general.columns:
    m, s = pivot_mean_std(agg_general, "cpu_max_during_norm")
    plot_lines_with_table(
        m, s,
        "",  # sem título
        "CPU máxima normalizada (%)",
        "cpu_vs_tamanho_all"
    )

# 3) RAM PICO – geral (sem NP-Completo)
if HAS_RAM_PEAK and "ram_peak_mb_mean" in agg_general.columns:
    m, s = pivot_mean_std(agg_general, "ram_peak_mb")
    plot_lines_with_table(
        m, s,
        "",  # sem título
        "RAM pico (MB)",
        "ram_vs_tamanho_all"
    )

# ===================== 4) Qualidade – NP-Completo (tempo) =====================
def is_small_or_medium_size(val: str) -> bool:
    s = str(val).strip().lower()
    if s in {"small", "pequeno", "medium", "medio"}:
        return True
    n = parse_k_suffix(s)
    if n is not None:
        return n <= 10_000
    if s in {"10^3", "10³"}:
        return True
    if s in {"10^4", "10⁴"}:
        return True
    return False

if {"classe", "algoritmo_norm", "tamanho", "tempo_s"}.issubset(df.columns):
    # Apenas NP-Completo e {exato, heurístico}
    base = df[(df["classe"].str.lower() == "np-completo") &
              (df["algoritmo_norm"].isin({"exato"} | GREEDY_ALIASES))].copy()

    if not base.empty:
        # small/medium para todos + large SOMENTE p/ heurístico
        mask_sm = base["tamanho"].apply(is_small_or_medium_size)
        mask_large = base["tamanho"].astype(str).str.lower().isin({"large", "grande"}) | (
            base["tamanho"].apply(parse_k_suffix).fillna(-1) > 10_000
        )
        is_greedy = base["algoritmo_norm"].isin(GREEDY_ALIASES)
        knap = base[mask_sm | (is_greedy & mask_large)].copy()

        # agrega por tamanho × algoritmo (tempo)
        qual_t = (knap.groupby(["tamanho", "algoritmo_norm"], as_index=False)
                        .agg(tempo_s_mean=("tempo_s", "mean"),
                             tempo_s_std=("tempo_s", "std"),
                             n=("tempo_s", "count")))
        # ordena tamanhos e salva
        qual_t["__ord_tam__"] = qual_t["tamanho"].apply(size_sort_key)
        qual_t = qual_t.sort_values(["__ord_tam__", "algoritmo_norm"]).drop(columns="__ord_tam__")

        # ---- Pivot (Exato vs Heurístico) ----
        pm = qual_t.pivot_table(index="tamanho", columns="algoritmo_norm",
                                values="tempo_s_mean", aggfunc="mean")
        ps = qual_t.pivot_table(index="tamanho", columns="algoritmo_norm",
                                values="tempo_s_std", aggfunc="mean")

        # reindex ordenado e alinhar
        idx_sizes = sorted(pm.index.unique(), key=size_sort_key)
        pm = pm.reindex(idx_sizes)
        ps = ps.reindex(idx_sizes)

        # localizar colunas
        cols = {c.lower(): c for c in pm.columns}
        c_exato = cols.get("exato")
        c_heur = None
        for alias in GREEDY_ALIASES:
            if alias in cols:
                c_heur = cols[alias]; break

        # salvar CSVs
        qual_t.to_csv(os.path.join(OUT_DIR, "qualidade_npcompleto_sm+heur_large_tempo_raw.csv"), index=False)
        pm.to_csv(os.path.join(OUT_DIR, "qualidade_npcompleto_sm+heur_large_tempo_mean_pivot.csv"))
        if ps is not None:
            ps.to_csv(os.path.join(OUT_DIR, "qualidade_npcompleto_sm+heur_large_tempo_std_pivot.csv"))

        # speedup (large ficará NaN no exato)
        if c_exato is not None and c_heur is not None:
            spd = pd.DataFrame({
                "tamanho": [str(i) for i in pm.index],
                "tempo_exato_mean": pm.get(c_exato),
                "tempo_heur_mean":  pm.get(c_heur),
            })
            spd["speedup_exato_div_heur"] = spd["tempo_exato_mean"] / spd["tempo_heur_mean"]
            spd["ganho_percent"] = (spd["tempo_exato_mean"] - spd["tempo_heur_mean"]) / spd["tempo_exato_mean"] * 100.0
            spd.to_csv(os.path.join(OUT_DIR, "npcompleto_sm+heur_large_speedup.csv"), index=False)

        # ---- Plot (linhas) – Exato vs Heurístico (tempo) + tabela separada ----
        def plot_quality_time(mean_df: pd.DataFrame, std_df: pd.DataFrame,
                              title: str, ylabel: str, filename: str):
            if mean_df is None or mean_df.empty:
                return
            x = np.arange(len(mean_df.index))
            plt.figure(figsize=(12, 6))
            colors = {c: COLORS_VIBRANT[i % len(COLORS_VIBRANT)] for i, c in enumerate(mean_df.columns)}
            for col in mean_df.columns:
                y = mean_df[col].values.astype(float)
                yerr = std_df[col].values.astype(float) if (std_df is not None and col in std_df.columns) else None
                plt.errorbar(x, y, yerr=yerr, fmt='-o', linewidth=1.8, markersize=5,
                             color=colors[col], ecolor=colors[col], capsize=4, label=str(col))
            # (sem título)
            plt.xlabel("Tamanho (small/medium + large só heurístico)")
            plt.ylabel(ylabel)
            plt.xticks(x, [str(v) for v in mean_df.index])
            plt.grid(True, axis='y', alpha=0.25)
            plt.legend(ncol=2, title="Algoritmo", loc="upper left",
                       bbox_to_anchor=(1.02, 1.0), borderaxespad=0.0)

            savefig(os.path.join(OUT_DIR, f"{filename}.png"), tight=True)

            # tabela separada (M/DP), exibindo "Indet." quando NaN
            # preparamos cópias com strings já formatadas
            tbl_mean = mean_df.copy()
            tbl_std  = std_df.copy() if std_df is not None else None
            # converter NaN -> "Indet." na mean
            for c in tbl_mean.columns:
                tbl_mean[c] = tbl_mean[c].astype(float)
            _table_to_png(tbl_mean, tbl_std, filename_base=filename, index_name="Tamanho")

        ps_aligned = ps.reindex(index=pm.index, columns=pm.columns) if ps is not None else None

        # Para a tabela da qualidade, queremos “Indet.” nos NaNs do exato/large:
        # Isso é feito na função _table_to_png ao converter DP vazio e mantendo NaN (renderizado como célula vazia)
        plot_quality_time(
            pm, ps_aligned,
            "",  # sem título
            "Tempo (s)",
            "qualidade_npcompleto_sm+heur_large_tempo"
        )
else:
    print("⚠️ Qualidade (NP-Completo): verifique 'classe', 'algoritmo_norm', 'tamanho', 'tempo_s'.")

# ===================== 5) Linhas de código por linguagem × algoritmo =====================
if "linhas_codigo" in df.columns and {"linguagem", "algoritmo"}.issubset(df.columns):
    loc_lang_alg = (df.groupby(["linguagem","algoritmo"])["linhas_codigo"]
                      .mean().unstack().fillna(0).sort_index())
    loc_lang_alg.to_csv(os.path.join(OUT_DIR, "linhas_codigo_linguagem_algoritmo.csv"))
    ax = loc_lang_alg.plot(kind="bar", figsize=(12,6), title="")  # sem título
    plt.ylabel("Linhas de código (média)")
    plt.xlabel("Linguagem")
    plt.xticks(rotation=45)
    for cont in ax.containers:
        ax.bar_label(cont, fmt="%.0f", fontsize=8)
    savefig(os.path.join(OUT_DIR, "linhas_codigo_linguagem_algoritmo.png"))

print("✅ BI concluído. Saída em:", OUT_DIR)
