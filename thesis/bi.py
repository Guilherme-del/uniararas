# -*- coding: utf-8 -*- 
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ===================== Config fixo =====================
OUT_DIR = "./bi"
os.makedirs(OUT_DIR, exist_ok=True)

# layout de tabela separada
TABLE_FONT_SIZE = 14
TABLE_SCALE_Y = 1.5

# legenda fora, à direita
LEGEND_NCOL = 1  # Uma coluna só para legenda mais legível

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
    "c": "C", "javascript": "JS", "typescript": "TS", 
    "csharp": "C#", "c#": "C#", "cpp": "C++", "c++": "C++",
    "golang": "Go", "python": "Py",
}

GREEDY_ALIASES = {
    "guloso", "greedy", "heuristica", "heurístico", "heuristico",
    "aproximacao", "aproximação", "approx", "heuristic"
}

# ===================== Configurações de estilo SUPER GRANDE =====================
PLOT_STYLE = {
    'marker_size': 25,           # MUITO GRANDE
    'line_width': 6.0,           # MUITO GROSSA
    'capsize': 15,               # MUITO GRANDE
    'font_size_labels': 24,      # MUITO GRANDE
    'font_size_ticks': 20,       # MUITO GRANDE
    'font_size_legend': 20,      # MUITO GRANDE
    'fig_size': (24, 16),        # MUITO GRANDE
    'dpi': 300,
}

# Configuração ESPECIAL para tempo vs tamanho
TIME_PLOT_STYLE = {
    'marker_size': 30,           # EXTRA GRANDE para tempo
    'line_width': 8.0,           # EXTRA GROSSA
    'capsize': 20,               # EXTRA GRANDE
    'font_size_labels': 28,      # EXTRA GRANDE
    'font_size_ticks': 24,       # EXTRA GRANDE
    'font_size_legend': 24,      # EXTRA GRANDE
    'fig_size': (28, 20),        # EXTRA GRANDE
    'dpi': 300,
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
        plt.savefig(path, dpi=PLOT_STYLE['dpi'], bbox_inches='tight', pad_inches=2.0)  # Mais padding
    else:
        plt.tight_layout()
        plt.savefig(path, dpi=PLOT_STYLE['dpi'])
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
HAS_RAM_PEAK = "ram_peak_mb" in df.columns

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
    std_col = f"{value_prefix}_std"
    
    if (mean_col not in agg_df.columns) or (std_col not in agg_df.columns):
        return None, None
    
    m = agg_df.pivot_table(index=index_col, columns=column_col, values=mean_col, aggfunc="mean")
    s = agg_df.pivot_table(index=index_col, columns=column_col, values=std_col, aggfunc="mean")
    
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
        table_df[f"{short_label(c)} – M"] = np.round(mean_df[c].values, 4)
        table_df[f"{short_label(c)} – DP"] = np.round(std_df[c].values, 4) if std_df is not None else np.nan
    
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
            row += [f"{mval:.4f}", ("" if (sval is None or np.isnan(sval)) else f"{sval:.4f}")]
        body.append(row)
    
    ncols = 1 + 2 * len(langs)
    w0 = 0.16
    w_each = (1.0 - w0) / (ncols - 1)
    colw = [w0] + [w_each] * (ncols - 1)
    
    fig_w = 24
    fig_h = 6 + 0.8 * max(1, len(body))
    
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
    
    plt.savefig(os.path.join(OUT_DIR, f"{filename_base}_table.png"), dpi=PLOT_STYLE['dpi'], bbox_inches="tight")
    plt.close(fig_tab)

def plot_lines_with_table(mean_df, std_df, title, ylabel, filename, is_time_plot=False):
    """Gera gráfico (sem título) e tabela separada (PNG + CSV)."""
    if mean_df is None or mean_df.empty:
        return
    
    # ---------- gráfico ----------
    x = np.arange(len(mean_df.index))
    
    # Usar estilo ESPECIAL para gráfico de tempo
    if is_time_plot:
        style = TIME_PLOT_STYLE
        print(f"🎯 Criando gráfico de tempo SUPER GRANDE: {filename}")
    else:
        style = PLOT_STYLE
    
    # Usar tamanho de figura MUITO GRANDE
    plt.figure(figsize=style['fig_size'])
    
    colors = {c: COLORS_VIBRANT[i % len(COLORS_VIBRANT)] for i, c in enumerate(mean_df.columns)}
    
    # PRIMEIRO configurar o grid com linhas PRETAS
    plt.grid(True, axis='y', alpha=0.3, linestyle='-', linewidth=1.5, color='black')
    plt.grid(True, axis='x', alpha=0.2, linestyle='-', linewidth=1.5, color='black')
    
    # DEPOIS plotar as linhas das linguagens com cores
    for col in mean_df.columns:
        y = mean_df[col].values
        yerr = std_df[col].values if (std_df is not None and col in std_df.columns) else None
        
        plt.errorbar(
            x, y, yerr=yerr,
            fmt='-o', 
            linewidth=style['line_width'],      
            markersize=style['marker_size'],    
            color=colors[col],
            ecolor=colors[col],
            capsize=style['capsize'],           
            label=str(col),
            markeredgewidth=5,                       # Borda EXTRA grossa
            alpha=0.9,
            markerfacecolor='white',                 # Fundo branco para máximo contraste
            markeredgecolor=colors[col],             # Borda colorida
            zorder=3                                 # Trazer para frente
        )
    
    # Configurações de estilo MUITO GRANDES
    plt.xlabel("Tamanho do dataset", fontsize=style['font_size_labels'], fontweight='bold')
    plt.ylabel(ylabel, fontsize=style['font_size_labels'], fontweight='bold')
    plt.xticks(x, [str(v) for v in mean_df.index], fontsize=style['font_size_ticks'])
    plt.yticks(fontsize=style['font_size_ticks'])
    
    # ESCALA FLEXÍVEL que se adapta aos dados
    if is_time_plot:
        max_val = mean_df.max().max()
        min_val = mean_df.min().min()
        
        print(f"📊 Ajustando escala para tempo: Mín={min_val:.4f}, Máx={max_val:.4f}")
        
        # Definir limites baseados nos dados reais
        if max_val <= 0.5:
            # Se tudo está abaixo de 0.5, manter escala expandida
            y_max = 0.55
            y_ticks = np.arange(0, 0.6, 0.05)
        elif max_val <= 1.0:
            # Se está entre 0.5 e 1.0
            y_max = 1.1
            y_ticks = np.arange(0, 1.2, 0.1)
        elif max_val <= 3.0:
            # Se está entre 1.0 e 3.0 (incluindo os 3 segundos)
            y_max = 3.5
            y_ticks = np.arange(0, 3.6, 0.5)
        elif max_val <= 5.0:
            # Se está entre 3.0 e 5.0
            y_max = 5.5
            y_ticks = np.arange(0, 6.0, 1.0)
        else:
            # Para valores maiores, usar escala com margem
            y_max = max_val * 1.15
            # Criar ticks apropriados para a escala
            step = max(1.0, y_max / 10)
            y_ticks = np.arange(0, y_max + step, step)
        
        plt.ylim(-0.05, y_max)
        plt.yticks(y_ticks)
        
        # Adicionar linhas horizontais de referência PRETAS
        if y_max <= 1.0:
            for y_val in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
                if y_val <= y_max:
                    plt.axhline(y=y_val, color='black', linestyle=':', alpha=0.2, linewidth=1)
        elif y_max <= 3.5:
            for y_val in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]:
                if y_val <= y_max:
                    plt.axhline(y=y_val, color='black', linestyle=':', alpha=0.2, linewidth=1)
        else:
            for y_val in [1.0, 2.0, 3.0, 4.0, 5.0]:
                if y_val <= y_max:
                    plt.axhline(y=y_val, color='black', linestyle=':', alpha=0.2, linewidth=1)
                    
    else:
        # Para outros gráficos, ajustar automaticamente
        y_min = mean_df.min().min()
        y_max = mean_df.max().max()
        margin = (y_max - y_min) * 0.2  # Mais margem
        plt.ylim(max(0, y_min - margin), y_max + margin)
    
    # Legenda MUITO GRANDE e bem posicionada
    legend = plt.legend(
        ncol=LEGEND_NCOL, 
        title="Linguagens", 
        loc="upper left", 
        bbox_to_anchor=(1.02, 1.0), 
        borderaxespad=0.0,
        fontsize=style['font_size_legend'],
        title_fontsize=style['font_size_legend'],
        framealpha=0.95,
        frameon=True,
        edgecolor='black'
    )
    
    # Melhorar MUITO a aparência geral
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_linewidth(3.0)    # MUITO grossa
    ax.spines['bottom'].set_linewidth(3.0)  # MUITO grossa
    
    # ESPAÇAMENTO MÁXIMO entre os pontos do eixo X
    plt.xlim(-0.8, len(mean_df.index) - 0.2)
    
    # Aumentar ESPAÇAMENTO entre ticks
    plt.tick_params(axis='x', which='major', pad=15)
    plt.tick_params(axis='y', which='major', pad=15)
    
    # Background mais claro para melhor contraste
    ax.set_facecolor('#f8f9fa')
    
    savefig(os.path.join(OUT_DIR, f"{filename}.png"), tight=True)
    
    # ---------- tabela separada ----------
    _table_to_png(mean_df, std_df, filename_base=filename, index_name="Tamanho")

# ===================== Agregações (GERAIS, sem NP-Completo) =====================
agg_general = build_agg(df_general)

# 1) TEMPO – geral (sem NP-Completo) - SUPER GRANDE E EXPANDIDO
m, s = pivot_mean_std(agg_general, "tempo_s")
if m is not None and not m.empty:
    max_val = m.max().max()
    min_val = m.min().min()
    print(f"📊 Valores de tempo - Mín: {min_val:.4f}, Máx: {max_val:.4f}")
    
    # SEMPRE usar estilo especial para tempo, independente do valor máximo
    plot_lines_with_table(
        m, s,
        "",  
        "Tempo (s)", 
        "tempo_vs_tamanho_all",
        is_time_plot=True  # Usar estilo ESPECIAL para tempo
    )
    print(f"✅ Gráfico de tempo SUPER GRANDE criado (escala adaptada até {max_val:.2f}s)")

# 2) CPU MÁXIMA NORMALIZADA – geral (sem NP-Completo)
if HAS_CPU_MAX_NORM and "cpu_max_during_norm_mean" in agg_general.columns:
    m, s = pivot_mean_std(agg_general, "cpu_max_during_norm")
    plot_lines_with_table(
        m, s,
        "",  
        "CPU máxima normalizada (%)", 
        "cpu_vs_tamanho_all",
        is_time_plot=False
    )

# 3) RAM PICO – geral (sem NP-Completo)
if HAS_RAM_PEAK and "ram_peak_mb_mean" in agg_general.columns:
    m, s = pivot_mean_std(agg_general, "ram_peak_mb")
    plot_lines_with_table(
        m, s,
        "",  
        "RAM pico (MB)", 
        "ram_vs_tamanho_all",
        is_time_plot=False
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
        pm = qual_t.pivot_table(index="tamanho", columns="algoritmo_norm", values="tempo_s_mean", aggfunc="mean")
        ps = qual_t.pivot_table(index="tamanho", columns="algoritmo_norm", values="tempo_s_std", aggfunc="mean")
        
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
                "tempo_heur_mean": pm.get(c_heur),
            })
            spd["speedup_exato_div_heur"] = spd["tempo_exato_mean"] / spd["tempo_heur_mean"]
            spd["ganho_percent"] = (spd["tempo_exato_mean"] - spd["tempo_heur_mean"]) / spd["tempo_exato_mean"] * 100.0
            spd.to_csv(os.path.join(OUT_DIR, "npcompleto_sm+heur_large_speedup.csv"), index=False)
        
        # ---- Plot (linhas) – Exato vs Heurístico (tempo) + tabela separada ----
        def plot_quality_time(mean_df: pd.DataFrame, std_df: pd.DataFrame, title: str, ylabel: str, filename: str):
            if mean_df is None or mean_df.empty:
                return
            
            x = np.arange(len(mean_df.index))
            plt.figure(figsize=PLOT_STYLE['fig_size'])
            
            colors = {c: COLORS_VIBRANT[i % len(COLORS_VIBRANT)] for i, c in enumerate(mean_df.columns)}
            
            # PRIMEIRO configurar o grid com linhas PRETAS
            plt.grid(True, axis='y', alpha=0.3, linestyle='-', linewidth=1.5, color='black')
            plt.grid(True, axis='x', alpha=0.2, linestyle='-', linewidth=1.5, color='black')
            
            # DEPOIS plotar as linhas dos algoritmos com cores
            for col in mean_df.columns:
                y = mean_df[col].values.astype(float)
                yerr = std_df[col].values.astype(float) if (std_df is not None and col in std_df.columns) else None
                
                plt.errorbar(
                    x, y, yerr=yerr,
                    fmt='-o',
                    linewidth=PLOT_STYLE['line_width'],
                    markersize=PLOT_STYLE['marker_size'],
                    color=colors[col],
                    ecolor=colors[col],
                    capsize=PLOT_STYLE['capsize'],
                    label=str(col),
                    markeredgewidth=4,
                    alpha=0.9,
                    markerfacecolor='white',
                    markeredgecolor=colors[col],
                    zorder=3
                )
            
            # Configurações para TCC
            plt.xlabel("Tamanho (small/medium + large só heurístico)", fontsize=PLOT_STYLE['font_size_labels'], fontweight='bold')
            plt.ylabel(ylabel, fontsize=PLOT_STYLE['font_size_labels'], fontweight='bold')
            plt.xticks(x, [str(v) for v in mean_df.index], fontsize=PLOT_STYLE['font_size_ticks'])
            plt.yticks(fontsize=PLOT_STYLE['font_size_ticks'])
            
            # Ajustar escala Y para melhor visualização
            y_min = mean_df.min().min()
            y_max = mean_df.max().max()
            margin = (y_max - y_min) * 0.2
            plt.ylim(max(0, y_min - margin), y_max + margin)
            
            legend = plt.legend(
                ncol=1, 
                title="Algoritmo", 
                loc="upper left", 
                bbox_to_anchor=(1.02, 1.0), 
                borderaxespad=0.0,
                fontsize=PLOT_STYLE['font_size_legend'],
                title_fontsize=PLOT_STYLE['font_size_legend'],
                framealpha=0.9
            )
            
            # Melhorar aparência
            ax = plt.gca()
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['left'].set_linewidth(2.0)
            ax.spines['bottom'].set_linewidth(2.0)
            ax.set_facecolor('#f8f9fa')
            
            savefig(os.path.join(OUT_DIR, f"{filename}.png"), tight=True)
            
            # tabela separada
            tbl_mean = mean_df.copy()
            tbl_std = std_df.copy() if std_df is not None else None
            
            _table_to_png(tbl_mean, tbl_std, filename_base=filename, index_name="Tamanho")
        
        ps_aligned = ps.reindex(index=pm.index, columns=pm.columns) if ps is not None else None
        
        plot_quality_time(
            pm, ps_aligned,
            "",  
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
    
    # TAMANHO ORIGINAL para gráfico de barras (não usar o tamanho gigante)
    plt.figure(figsize=(12, 6))  # Tamanho original padrão
    
    ax = loc_lang_alg.plot(kind="bar", title="")
    plt.ylabel("Linhas de código (média)", fontsize=14, fontweight='bold')
    plt.xlabel("Linguagem", fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(fontsize=12)
    
    # Configurar grid PRETO para o gráfico de barras
    plt.grid(True, axis='y', alpha=0.3, linestyle='-', linewidth=1.0, color='black')
    
    # Melhorar barras
    for cont in ax.containers:
        ax.bar_label(cont, fmt="%.0f", fontsize=10, fontweight='bold', padding=3)
    
    # Melhorar aparência
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_linewidth(1.0)
    ax.spines['bottom'].set_linewidth(1.0)
    ax.set_facecolor('#f8f9fa')
    
    savefig(os.path.join(OUT_DIR, "linhas_codigo_linguagem_algoritmo.png"))
    