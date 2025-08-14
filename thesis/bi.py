import pandas as pd
import matplotlib.pyplot as plt
import os

# Criar pasta de saída
os.makedirs("./bi", exist_ok=True)

# Carrega o JSON
df = pd.read_json("./resultados/metricas.json")

# Filtra apenas entradas com tempo válido
df = df[df["tempo_s"] > 0]

# Função para desenhar gráfico de barras com valores
def plot_with_labels(data, title, ylabel, filename):
    ax = data.plot(kind="bar", figsize=(10, 6), title=title)
    plt.ylabel(ylabel)
    plt.xlabel(data.index.name)
    plt.xticks(rotation=45)
    for c in ax.containers:
        ax.bar_label(c, fmt="%.2f", fontsize=8)
    plt.tight_layout()
    plt.savefig(f"./bi/{filename}.png")
    plt.clf()

# Grouping
grouped = df.groupby(["linguagem", "tamanho"])

# Tempo médio por linguagem e tamanho
tempo_medio = grouped["tempo_s"].mean().unstack()
tempo_medio.to_csv("./bi/tabela_tempo_medio.csv")
plot_with_labels(tempo_medio, "Tempo Médio (s) por Linguagem e Tamanho", "Tempo (s)", "tempo_medio_por_tamanho")

# CPU média durante execução
cpu_medio = grouped["cpu_avg_during"].mean().unstack()
cpu_medio.to_csv("./bi/tabela_cpu_medio.csv")
plot_with_labels(cpu_medio, "CPU Média Durante Execução por Linguagem e Tamanho", "Uso de CPU (%)", "cpu_medio_por_tamanho")

# RAM média durante execução
ram_medio = grouped["ram_avg_during_mb"].mean().unstack()
ram_medio.to_csv("./bi/tabela_ram_medio.csv")
plot_with_labels(ram_medio, "RAM Média Durante Execução por Linguagem e Tamanho", "RAM (MB)", "ram_medio_por_tamanho")

# Linhas de código por linguagem (média)
linhas_codigo = df.groupby("linguagem")["linhas_codigo"].mean().sort_values()
linhas_codigo.to_csv("./bi/tabela_linhas_codigo.csv")
plot_with_labels(linhas_codigo.to_frame(), "Média de Linhas de Código por Linguagem", "Linhas", "linhas_codigo_por_linguagem")

# Tempo médio por classe polinomial
tempo_classe = df.groupby("classe")["tempo_s"].mean().sort_values()
tempo_classe.to_csv("./bi/tabela_tempo_por_classe.csv")
plot_with_labels(tempo_classe.to_frame(), "Tempo Médio por Classe de Complexidade", "Tempo (s)", "tempo_medio_por_classe")

# Linhas de código por linguagem e classe polinomial (média)
linhas_codigo_linguagem_classe = df.groupby(["linguagem", "classe"])["linhas_codigo"].mean().unstack()
linhas_codigo_linguagem_classe.to_csv("./bi/tabela_linhas_codigo_linguagem_classe.csv")
plot_with_labels(
    linhas_codigo_linguagem_classe,
    "Média de Linhas de Código por Linguagem e Classe Polinomial",
    "Linhas de Código",
    "linhas_codigo_por_linguagem_e_classe"
)
