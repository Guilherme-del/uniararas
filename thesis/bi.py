# -*- coding: utf-8 -*- 
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

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

# ===================== Configurações de estilo =====================
PLOT_STYLE = {
    'marker_size': 25,           
    'line_width': 6.0,           
    'capsize': 15,               
    'font_size_labels': 24,     
    'font_size_ticks': 20,       
    'font_size_legend': 20,      
    'fig_size': (28, 16),        
    'dpi': 300,
}

# Configuração ESPECIAL para tempo vs tamanho
TIME_PLOT_STYLE = {
    'marker_size': 30,           
    'line_width': 3.0,          
    'capsize': 2,              
    'font_size_labels': 28,      
    'font_size_ticks': 24,       
    'font_size_legend': 24,    
    'fig_size': (32, 20),        
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
        plt.savefig(path, dpi=PLOT_STYLE['dpi'], bbox_inches='tight', pad_inches=2.0)
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

def plot_bars_with_table(mean_df, std_df, title, ylabel, filename, is_time_plot=False):
    """Gera gráfico de barras agrupadas (sem título) e tabela separada."""
    if mean_df is None or mean_df.empty:
        return
    
    # Configurações de estilo
    if is_time_plot:
        style = TIME_PLOT_STYLE
    else:
        style = PLOT_STYLE
    
    plt.figure(figsize=style['fig_size'])
    
    colors = {c: COLORS_VIBRANT[i % len(COLORS_VIBRANT)] for i, c in enumerate(mean_df.columns)}
    
    # Configurar posições das barras
    n_groups = len(mean_df.index)
    n_bars = len(mean_df.columns)
    bar_width = 0.8 / n_bars  # Largura dinâmica baseada no número de barras
    
    x_positions = np.arange(n_groups)
    
    # Plotar barras para cada linguagem
    for i, col in enumerate(mean_df.columns):
        bar_pos = x_positions + i * bar_width - (n_bars * bar_width) / 2 + bar_width / 2
        y_values = mean_df[col].values
        y_errors = std_df[col].values if (std_df is not None and col in std_df.columns) else None
        
        plt.bar(
            bar_pos, 
            y_values,
            width=bar_width,
            color=colors[col],
            edgecolor='black',
            linewidth=2,
            alpha=0.8,
            label=str(col),
            yerr=y_errors,
            capsize=5,
            error_kw={'elinewidth': 2, 'capthick': 2}
        )
        
        # Adicionar valores nas barras se o espaço permitir
        max_val = mean_df.max().max()
        if max_val > 0:  # Só adiciona texto se não for zero
            for j, v in enumerate(y_values):
                if v > max_val * 0.05:  # Só mostra texto se for significativo
                    plt.text(bar_pos[j], v + max_val * 0.01, f'{v:.3f}', 
                            ha='center', va='bottom', fontsize=style['font_size_ticks']-4,
                            fontweight='bold')

    # Configurações do gráfico
    plt.xlabel("Tamanho do dataset", fontsize=style['font_size_labels'], fontweight='bold')
    plt.ylabel(ylabel, fontsize=style['font_size_labels'], fontweight='bold')
    
    # Configurar eixo X
    plt.xticks(x_positions, [str(v) for v in mean_df.index], fontsize=style['font_size_ticks'])
    plt.xlim(x_positions[0] - 0.5, x_positions[-1] + 0.5)
    
    # Configurar eixo Y com mais espaço
    y_min = mean_df.min().min()
    y_max = mean_df.max().max()
    margin = (y_max - y_min) * 0.3
    plt.ylim(max(0, y_min - margin), y_max + margin)
    
    # Grid mais sutil
    plt.grid(True, axis='y', alpha=0.2, linestyle='-', linewidth=1.0, color='black')
    plt.grid(False, axis='x')
    
    # Legenda
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
    
    # Melhorar aparência
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_linewidth(2.0)
    ax.spines['bottom'].set_linewidth(2.0)
    ax.set_facecolor('#f8f9fa')
    
    savefig(os.path.join(OUT_DIR, f"{filename}_barras.png"), tight=True)
    
    # Tabela separada
    _table_to_png(mean_df, std_df, filename_base=f"{filename}_barras", index_name="Tamanho")

def plot_heatmap_with_table(mean_df, std_df, title, ylabel, filename):
    """Gera heatmap para visualização de valores próximos."""
    if mean_df is None or mean_df.empty:
        return
    
    plt.figure(figsize=(16, 10))
    
    # Criar heatmap
    im = plt.imshow(mean_df.values.T, cmap='YlOrRd', aspect='auto')
    
    # Configurar ticks
    plt.xticks(np.arange(len(mean_df.index)), mean_df.index, fontsize=16)
    plt.yticks(np.arange(len(mean_df.columns)), mean_df.columns, fontsize=16)
    
    # Adicionar valores nas células
    for i in range(len(mean_df.index)):
        for j in range(len(mean_df.columns)):
            text = plt.text(i, j, f'{mean_df.iloc[i, j]:.4f}',
                           ha="center", va="center", color="black", fontsize=14, fontweight='bold')
    
    plt.xlabel("Tamanho do dataset", fontsize=18, fontweight='bold')
    plt.ylabel("Linguagens", fontsize=18, fontweight='bold')
    
    # Barra de cores
    cbar = plt.colorbar(im)
    cbar.set_label(ylabel, fontsize=16)
    
    plt.tight_layout()
    savefig(os.path.join(OUT_DIR, f"{filename}_heatmap.png"), tight=True)

def plot_dot_plot_with_table(mean_df, std_df, title, ylabel, filename):
    """Gráfico de pontos com linhas de referência para valores próximos."""
    if mean_df is None or mean_df.empty:
        return
    
    plt.figure(figsize=(20, 12))
    
    colors = {c: COLORS_VIBRANT[i % len(COLORS_VIBRANT)] for i, c in enumerate(mean_df.columns)}
    
    # Criar grid de linhas de referência
    y_min = mean_df.min().min()
    y_max = mean_df.max().max()
    
    # Linhas de referência mais densas
    y_range = y_max - y_min
    step = y_range / 20  # Mais linhas para melhor referência
    
    for y_val in np.arange(y_min, y_max + step, step):
        plt.axhline(y=y_val, color='gray', linestyle='--', alpha=0.3, linewidth=0.5)
    
    # Plotar pontos para cada linguagem
    for col in mean_df.columns:
        x_positions = np.arange(len(mean_df.index))
        y_values = mean_df[col].values
        
        plt.scatter(
            x_positions, y_values,
            s=200,  # Tamanho dos pontos
            color=colors[col],
            edgecolor='black',
            linewidth=2,
            alpha=0.8,
            label=str(col),
            zorder=5
        )
        
        # Conectar pontos com linhas finas
        plt.plot(x_positions, y_values, 
                color=colors[col], 
                linewidth=1, 
                alpha=0.5,
                zorder=4)
        
        # Adicionar valores aos pontos
        for i, (x, y) in enumerate(zip(x_positions, y_values)):
            plt.text(x, y + y_range * 0.01, f'{y:.4f}', 
                    ha='center', va='bottom', 
                    fontsize=12, fontweight='bold',
                    bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))
    
    plt.xlabel("Tamanho do dataset", fontsize=16, fontweight='bold')
    plt.ylabel(ylabel, fontsize=16, fontweight='bold')
    plt.xticks(np.arange(len(mean_df.index)), mean_df.index, fontsize=14)
    plt.yticks(fontsize=14)
    
    # Ajustar limites
    plt.xlim(-0.5, len(mean_df.index) - 0.5)
    margin = (y_max - y_min) * 0.15
    plt.ylim(y_min - margin, y_max + margin)
    
    plt.legend(fontsize=14)
    plt.grid(True, alpha=0.2)
    
    savefig(os.path.join(OUT_DIR, f"{filename}_dotplot.png"), tight=True)

# ===================== GRÁFICOS ADICIONAIS =====================

def plot_radar_chart(mean_df, filename):
    """Gráfico de radar para comparar linguagens em múltiplas dimensões."""
    if mean_df is None or mean_df.empty:
        return
    
    # Preparar dados para radar
    metrics = list(mean_df.columns)
    languages = list(mean_df.index)
    
    # Normalizar os dados para escala 0-1
    df_normalized = mean_df.apply(lambda x: (x - x.min()) / (x.max() - x.min()), axis=0)
    
    # Ângulos para cada métrica
    angles = np.linspace(0, 2*np.pi, len(metrics), endpoint=False).tolist()
    angles += angles[:1]  # Fechar o círculo
    
    fig, ax = plt.subplots(figsize=(16, 12), subplot_kw=dict(projection='polar'))
    
    for i, lang in enumerate(languages):
        values = df_normalized.loc[lang].values.tolist()
        values += values[:1]  # Fechar o círculo
        
        ax.plot(angles, values, 'o-', linewidth=3, 
                label=lang, color=COLORS_VIBRANT[i % len(COLORS_VIBRANT)],
                markersize=8)
        ax.fill(angles, values, alpha=0.1, color=COLORS_VIBRANT[i % len(COLORS_VIBRANT)])
    
    # Configurar o gráfico
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(metrics, fontsize=12)
    ax.set_yticklabels([])
    ax.set_ylim(0, 1)
    
    plt.title('Comparação de Linguagens - Gráfico de Radar', size=16, fontweight='bold')
    plt.legend(bbox_to_anchor=(1.2, 1.0), loc='upper left')
    
    savefig(os.path.join(OUT_DIR, f"{filename}_radar.png"), tight=True)

def plot_boxplot_by_language(df, metric, ylabel, filename):
    """Boxplot mostrando distribuição por linguagem."""
    if metric not in df.columns:
        return
    
    plt.figure(figsize=(16, 10))
    
    # Preparar dados
    data = [df[df['linguagem'] == lang][metric].dropna() for lang in df['linguagem'].unique()]
    labels = df['linguagem'].unique()
    
    box_plot = plt.boxplot(data, labels=labels, patch_artist=True)
    
    # Cores para as caixas
    for i, box in enumerate(box_plot['boxes']):
        box.set_facecolor(COLORS_VIBRANT[i % len(COLORS_VIBRANT)])
        box.set_alpha(0.7)
    
    plt.ylabel(ylabel, fontsize=14, fontweight='bold')
    plt.xlabel('Linguagem', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    
    savefig(os.path.join(OUT_DIR, f"{filename}_boxplot.png"), tight=True)

def plot_correlation_heatmap(df, filename):
    """Heatmap de correlação entre métricas."""
    numeric_cols = ['tempo_s', 'cpu_max_during_norm', 'ram_peak_mb', 'linhas_codigo']
    numeric_cols = [col for col in numeric_cols if col in df.columns]
    
    if len(numeric_cols) < 2:
        return
    
    corr_matrix = df[numeric_cols].corr()
    
    plt.figure(figsize=(10, 8))
    im = plt.imshow(corr_matrix, cmap='coolwarm', aspect='auto', vmin=-1, vmax=1)
    
    # Adicionar anotações
    for i in range(len(corr_matrix)):
        for j in range(len(corr_matrix)):
            text = plt.text(j, i, f'{corr_matrix.iloc[i, j]:.2f}',
                          ha="center", va="center", color="white", 
                          fontsize=12, fontweight='bold')
    
    plt.xticks(range(len(corr_matrix)), corr_matrix.columns, rotation=45)
    plt.yticks(range(len(corr_matrix)), corr_matrix.columns)
    plt.colorbar(im)
    plt.title('Matriz de Correlação entre Métricas', fontsize=14, fontweight='bold')
    
    savefig(os.path.join(OUT_DIR, f"{filename}_correlacao.png"), tight=True)

def plot_violin_by_language(df, metric, ylabel, filename):
    """Gráfico de violino mostrando distribuição e densidade."""
    if metric not in df.columns:
        return
    
    plt.figure(figsize=(16, 10))
    
    data = []
    labels = []
    colors = []
    
    for i, lang in enumerate(df['linguagem'].unique()):
        lang_data = df[df['linguagem'] == lang][metric].dropna()
        if len(lang_data) > 0:
            data.append(lang_data)
            labels.append(lang)
            colors.append(COLORS_VIBRANT[i % len(COLORS_VIBRANT)])
    
    violin_parts = plt.violinplot(data, showmeans=True, showmedians=True)
    
    # Colorir os violinos
    for i, pc in enumerate(violin_parts['bodies']):
        pc.set_facecolor(colors[i])
        pc.set_alpha(0.7)
    
    plt.xticks(range(1, len(labels) + 1), labels, rotation=45)
    plt.ylabel(ylabel, fontsize=14, fontweight='bold')
    plt.xlabel('Linguagem', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    
    savefig(os.path.join(OUT_DIR, f"{filename}_violino.png"), tight=True)

def plot_scatter_metrics(df, x_metric, y_metric, filename):
    """Scatter plot entre duas métricas."""
    if x_metric not in df.columns or y_metric not in df.columns:
        return
    
    plt.figure(figsize=(14, 10))
    
    for i, lang in enumerate(df['linguagem'].unique()):
        lang_data = df[df['linguagem'] == lang]
        plt.scatter(
            lang_data[x_metric], 
            lang_data[y_metric],
            color=COLORS_VIBRANT[i % len(COLORS_VIBRANT)],
            label=lang,
            alpha=0.7,
            s=100,
            edgecolors='black',
            linewidth=1
        )
    
    plt.xlabel(x_metric.replace('_', ' ').title(), fontsize=14, fontweight='bold')
    plt.ylabel(y_metric.replace('_', ' ').title(), fontsize=14, fontweight='bold')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.3)
    
    # Adicionar linha de tendência
    z = np.polyfit(df[x_metric], df[y_metric], 1)
    p = np.poly1d(z)
    plt.plot(df[x_metric], p(df[x_metric]), "r--", alpha=0.8, linewidth=2)
    
    # Coeficiente de correlação
    corr = df[x_metric].corr(df[y_metric])
    plt.text(0.05, 0.95, f'Correlação: {corr:.3f}', 
             transform=plt.gca().transAxes, fontsize=12,
             bbox=dict(boxstyle="round", facecolor='white', alpha=0.8))
    
    savefig(os.path.join(OUT_DIR, f"{filename}_scatter.png"), tight=True)

def plot_trend_with_regression(mean_df, ylabel, filename):
    """Gráfico de tendência com linha de regressão."""
    if mean_df is None or mean_df.empty:
        return
    
    plt.figure(figsize=(18, 12))
    
    x_positions = np.arange(len(mean_df.index))
    
    for i, col in enumerate(mean_df.columns):
        y_values = mean_df[col].values
        
        # Plotar pontos originais
        plt.scatter(
            x_positions, y_values,
            color=COLORS_VIBRANT[i % len(COLORS_VIBRANT)],
            label=col,
            s=100,
            alpha=0.8,
            zorder=5
        )
        
        # Calcular e plotar regressão linear
        if len(y_values) > 1:
            z = np.polyfit(x_positions, y_values, 1)
            p = np.poly1d(z)
            plt.plot(x_positions, p(x_positions), 
                    color=COLORS_VIBRANT[i % len(COLORS_VIBRANT)],
                    linewidth=3, 
                    alpha=0.6,
                    linestyle='--',
                    label=f'{col} (tendência)')
    
    plt.xlabel("Tamanho do Dataset", fontsize=16, fontweight='bold')
    plt.ylabel(ylabel, fontsize=16, fontweight='bold')
    plt.xticks(x_positions, mean_df.index, fontsize=12)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.3)
    
    savefig(os.path.join(OUT_DIR, f"{filename}_tendencia.png"), tight=True)

def plot_stacked_area(mean_df, ylabel, filename):
    """Gráfico de área empilhada por linguagem."""
    if mean_df is None or mean_df.empty:
        return
    
    plt.figure(figsize=(20, 12))
    
    # Transpor para ter tamanhos no eixo X
    df_transposed = mean_df.T
    
    # Plotar área empilhada
    ax = df_transposed.plot.area(
        figsize=(20, 12),
        color=COLORS_VIBRANT[:len(df_transposed.columns)],
        alpha=0.8,
        linewidth=2
    )
    
    plt.xlabel('Tamanho do Dataset', fontsize=16, fontweight='bold')
    plt.ylabel(ylabel, fontsize=16, fontweight='bold')
    plt.legend(title='Linguagens', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.3)
    
    savefig(os.path.join(OUT_DIR, f"{filename}_area_empilhada.png"), tight=True)

# ===================== Agregações (GERAIS, sem NP-Completo) =====================
agg_general = build_agg(df_general)

# 1) TEMPO – geral (sem NP-Completo)
m, s = pivot_mean_std(agg_general, "tempo_s")
if m is not None and not m.empty:
    max_val = m.max().max()
    min_val = m.min().min()
    print(f"📊 Valores de tempo - Mín: {min_val:.4f}, Máx: {max_val:.4f}")
    
    # Gráfico de barras para tempo
    plot_bars_with_table(
        m, s,
        "",  
        "Tempo (s)", 
        "tempo_vs_tamanho_all",
        is_time_plot=True
    )
    
    # Heatmap complementar
    plot_heatmap_with_table(
        m, s,
        "",  
        "Tempo (s)", 
        "tempo_vs_tamanho_all"
    )
    
    # Gráfico de tendência com regressão
    plot_trend_with_regression(
        m,
        "Tempo (s)", 
        "tempo_vs_tamanho_all"
    )
    
    # Gráfico de área empilhada
    plot_stacked_area(
        m,
        "Tempo (s)", 
        "tempo_vs_tamanho_all"
    )
    
    print(f"✅ Gráficos de tempo criados (escala adaptada até {max_val:.2f}s)")

# 2) CPU MÁXIMA NORMALIZADA – geral (sem NP-Completo)
if HAS_CPU_MAX_NORM and "cpu_max_during_norm_mean" in agg_general.columns:
    m, s = pivot_mean_std(agg_general, "cpu_max_during_norm")
    
    # Gráfico de barras para CPU
    plot_bars_with_table(
        m, s,
        "",  
        "CPU máxima normalizada (%)", 
        "cpu_vs_tamanho_all",
        is_time_plot=False
    )
    
    # Dot plot para valores próximos
    plot_dot_plot_with_table(
        m, s,
        "",  
        "CPU máxima normalizada (%)", 
        "cpu_vs_tamanho_all"
    )
    
    # HEATMAP PARA CPU
    plot_heatmap_with_table(
        m, s,
        "",  
        "CPU máxima normalizada (%)", 
        "cpu_vs_tamanho_all"
    )
    
    print("✅ Gráficos de CPU criados (barras, dot plot e heatmap)")

# 3) RAM PICO – geral (sem NP-Completo)
if HAS_RAM_PEAK and "ram_peak_mb_mean" in agg_general.columns:
    m, s = pivot_mean_std(agg_general, "ram_peak_mb")
    
    # Gráfico de barras para RAM
    plot_bars_with_table(
        m, s,
        "",  
        "RAM pico (MB)", 
        "ram_vs_tamanho_all",
        is_time_plot=False
    )
    
    # Heatmap complementar
    plot_heatmap_with_table(
        m, s,
        "",  
        "RAM pico (MB)", 
        "ram_vs_tamanho_all"
    )
    
    print("✅ Gráficos de RAM criados (barras e heatmap)")

# ===================== GRÁFICOS ADICIONAIS GLOBAIS =====================

print("📊 Gerando gráficos adicionais...")

# 1. Radar Chart (se tiver múltiplas métricas)
if all(metric in df_general.columns for metric in ['tempo_s', 'cpu_max_during_norm', 'ram_peak_mb']):
    # Agrupar por linguagem e calcular médias
    radar_data = df_general.groupby('linguagem')[['tempo_s', 'cpu_max_during_norm', 'ram_peak_mb']].mean()
    plot_radar_chart(radar_data, "comparacao_linguagens")
    print("✅ Gráfico de radar criado")

# 2. Boxplots
plot_boxplot_by_language(df_general, 'tempo_s', 'Tempo (s)', 'tempo_boxplot')
print("✅ Boxplot de tempo criado")

if HAS_CPU_MAX_NORM:
    plot_boxplot_by_language(df_general, 'cpu_max_during_norm', 'CPU (%)', 'cpu_boxplot')
    print("✅ Boxplot de CPU criado")

if HAS_RAM_PEAK:
    plot_boxplot_by_language(df_general, 'ram_peak_mb', 'RAM (MB)', 'ram_boxplot')
    print("✅ Boxplot de RAM criado")

# 3. Gráficos de violino
plot_violin_by_language(df_general, 'tempo_s', 'Tempo (s)', 'tempo_violino')
print("✅ Gráfico de violino de tempo criado")

if HAS_CPU_MAX_NORM:
    plot_violin_by_language(df_general, 'cpu_max_during_norm', 'CPU (%)', 'cpu_violino')
    print("✅ Gráfico de violino de CPU criado")

# 4. Correlação
plot_correlation_heatmap(df_general, "correlacao_metricas")
print("✅ Heatmap de correlação criado")

# 5. Scatter Plots
plot_scatter_metrics(df_general, 'tempo_s', 'cpu_max_during_norm', 'tempo_vs_cpu')
print("✅ Scatter plot tempo vs CPU criado")

plot_scatter_metrics(df_general, 'tempo_s', 'ram_peak_mb', 'tempo_vs_ram')
print("✅ Scatter plot tempo vs RAM criado")

if HAS_CPU_MAX_NORM and HAS_RAM_PEAK:
    plot_scatter_metrics(df_general, 'cpu_max_during_norm', 'ram_peak_mb', 'cpu_vs_ram')
    print("✅ Scatter plot CPU vs RAM criado")

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
        
        # ---- Gráfico de barras para qualidade ----
        def plot_quality_bars(mean_df: pd.DataFrame, std_df: pd.DataFrame, title: str, ylabel: str, filename: str):
            if mean_df is None or mean_df.empty:
                return
            
            plt.figure(figsize=(20, 12))
            
            colors = {c: COLORS_VIBRANT[i % len(COLORS_VIBRANT)] for i, c in enumerate(mean_df.columns)}
            
            # Configurar posições das barras
            n_groups = len(mean_df.index)
            n_bars = len(mean_df.columns)
            bar_width = 0.8 / n_bars
            
            x_positions = np.arange(n_groups)
            
            # Plotar barras para cada algoritmo
            for i, col in enumerate(mean_df.columns):
                bar_pos = x_positions + i * bar_width - (n_bars * bar_width) / 2 + bar_width / 2
                y_values = mean_df[col].values.astype(float)
                y_errors = std_df[col].values.astype(float) if (std_df is not None and col in std_df.columns) else None
                
                plt.bar(
                    bar_pos, 
                    y_values,
                    width=bar_width,
                    color=colors[col],
                    edgecolor='black',
                    linewidth=2,
                    alpha=0.8,
                    label=str(col),
                    yerr=y_errors,
                    capsize=5,
                    error_kw={'elinewidth': 2, 'capthick': 2}
                )
                
                # Adicionar valores nas barras
                max_val = mean_df.max().max()
                if max_val > 0:
                    for j, v in enumerate(y_values):
                        if not np.isnan(v) and v > max_val * 0.05:
                            plt.text(bar_pos[j], v + max_val * 0.01, f'{v:.3f}', 
                                    ha='center', va='bottom', fontsize=16,
                                    fontweight='bold')

            # Configurações do gráfico
            plt.xlabel("Tamanho (small/medium + large só heurístico)", fontsize=20, fontweight='bold')
            plt.ylabel(ylabel, fontsize=20, fontweight='bold')
            
            # Configurar eixo X
            plt.xticks(x_positions, [str(v) for v in mean_df.index], fontsize=18)
            plt.xlim(x_positions[0] - 0.5, x_positions[-1] + 0.5)
            
            # Configurar eixo Y com mais espaço
            y_min = mean_df.min().min()
            y_max = mean_df.max().max()
            margin = (y_max - y_min) * 0.3
            plt.ylim(max(0, y_min - margin), y_max + margin)
            
            # Grid
            plt.grid(True, axis='y', alpha=0.2, linestyle='-', linewidth=1.0, color='black')
            plt.grid(False, axis='x')
            
            # Legenda
            legend = plt.legend(
                ncol=1, 
                title="Algoritmo", 
                loc="upper left", 
                bbox_to_anchor=(1.02, 1.0), 
                borderaxespad=0.0,
                fontsize=18,
                title_fontsize=18,
                framealpha=0.9
            )
            
            # Melhorar aparência
            ax = plt.gca()
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['left'].set_linewidth(2.0)
            ax.spines['bottom'].set_linewidth(2.0)
            ax.set_facecolor('#f8f9fa')
            
            savefig(os.path.join(OUT_DIR, f"{filename}_barras.png"), tight=True)
            
            # Tabela separada
            tbl_mean = mean_df.copy()
            tbl_std = std_df.copy() if std_df is not None else None
            _table_to_png(tbl_mean, tbl_std, filename_base=filename, index_name="Tamanho")    

        ps_aligned = ps.reindex(index=pm.index, columns=pm.columns) if ps is not None else None
        
        plot_quality_bars(
            pm, ps_aligned,
            "",  
            "Tempo (s)", 
            "qualidade_npcompleto_sm+heur_large_tempo"
        )
        
        # Heatmap para qualidade NP-Completo
        plot_heatmap_with_table(
            pm, ps_aligned,
            "",  
            "Tempo (s)", 
            "qualidade_npcompleto_sm+heur_large_tempo"
        )
        
        print("✅ Gráficos de qualidade NP-Completo criados (barras e heatmap)")
else:
    print("⚠️ Qualidade (NP-Completo): verifique 'classe', 'algoritmo_norm', 'tamanho', 'tempo_s'.")

# ===================== 5) Linhas de código por linguagem (média geral) =====================
if "linhas_codigo" in df.columns and "linguagem" in df.columns:
    # Agrupa apenas por linguagem, ignorando o algoritmo
    loc_lang = df.groupby("linguagem")["linhas_codigo"].agg(['mean', 'std', 'count']).round(2)
    loc_lang.to_csv(os.path.join(OUT_DIR, "linhas_codigo_linguagem.csv"))
    
    # Prepara dados para o gráfico de barras
    languages = loc_lang.index.tolist()
    means = loc_lang['mean'].values
    stds = loc_lang['std'].values
    
    # TAMANHO ORIGINAL para gráfico de barras
    plt.figure(figsize=(12, 6))
    
    # Gráfico de barras SEM as linhas de erro (removido yerr=stds)
    bars = plt.bar(languages, means, capsize=5, 
                   color=COLORS_VIBRANT[:len(languages)], 
                   edgecolor='black', linewidth=1.5, alpha=0.8)
    
    plt.ylabel("Linhas de código (média)", fontsize=14, fontweight='bold')
    plt.xlabel("Linguagem", fontsize=14, fontweight='bold')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    
    # Adicionar valores nas barras (mais limpo, sem as linhas pretas)
    for bar, mean_val in zip(bars, means):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,  # Pequeno espaço acima da barra
                f'{mean_val:.0f}', ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    # Configurar grid PRETO apenas horizontal
    plt.grid(True, axis='y', alpha=0.3, linestyle='-', linewidth=1.0, color='black')
    plt.grid(False, axis='x')  # Remove grid vertical
    
    # Melhorar aparência
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_linewidth(1.0)
    ax.spines['bottom'].set_linewidth(1.0)
    ax.set_facecolor('#f8f9fa')
    
    # Ajustar limites do eixo Y para dar espaço para os números
    y_max = max(means) * 1.15  # 15% de margem no topo
    plt.ylim(0, y_max)
    
    savefig(os.path.join(OUT_DIR, "linhas_codigo_linguagem.png"))
    
    print(f"✅ Gráfico de linhas de código por linguagem criado ({len(languages)} linguagens)")

print("\n🎉 TODOS OS GRÁFICOS FORAM GERADOS COM SUCESSO!")
print("="*60)
print("📊 RESUMO DOS GRÁFICOS CRIADOS:")
print("   📈 Gráficos de Barras Agrupadas (_barras.png)")
print("   🔥 Heatmaps (_heatmap.png)")
print("   📍 Dot Plots (_dotplot.png)")
print("   📉 Gráficos de Tendência (_tendencia.png)")
print("   📊 Áreas Empilhadas (_area_empilhada.png)")
print("   🎯 Radar Charts (_radar.png)")
print("   📦 Boxplots (_boxplot.png)")
print("   🎻 Gráficos de Violino (_violino.png)")
print("   🔗 Scatter Plots (_scatter.png)")
print("   📋 Tabelas em PNG e CSV")
print("="*60)
print("🔥 ANÁLISE COMPLETA DISPONÍVEL NA PASTA './bi/'")
