import pandas as pd
import matplotlib.pyplot as plt

# Carrega o JSON
df = pd.read_json("./resultados/metricas.json")

# Filtra entradas com tempo > 0
df = df[df["tempo_s"] > 0]

# Agrupamento por linguagem e tamanho
grouped = df.groupby(["linguagem", "tamanho"])

# Tempo médio por linguagem e tamanho
tempo_medio = grouped["tempo_s"].mean().unstack()
tempo_medio.plot(kind="bar", figsize=(10, 6), title="Tempo Médio (s) por Linguagem e Tamanho")
plt.ylabel("Tempo (s)")
plt.xlabel("Linguagem")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("./bi/tempo_medio_por_tamanho.png")
plt.clf()

# CPU média por linguagem e tamanho
cpu_medio = grouped["cpu_avg_during"].mean().unstack()
cpu_medio.plot(kind="bar", figsize=(10, 6), title="CPU Média Durante Execução por Linguagem e Tamanho")
plt.ylabel("Uso de CPU (%)")
plt.xlabel("Linguagem")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("./bi/cpu_medio_por_tamanho.png")
plt.clf()

# RAM média por linguagem e tamanho
ram_medio = grouped["ram_avg_during_mb"].mean().unstack()
ram_medio.plot(kind="bar", figsize=(10, 6), title="RAM Média Durante Execução por Linguagem e Tamanho")
plt.ylabel("RAM (MB)")
plt.xlabel("Linguagem")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("./bi/ram_medio_por_tamanho.png")
plt.clf()

# Linhas de código por linguagem
linhas_por_linguagem = df.groupby("linguagem")["linhas_codigo"].mean().sort_values()
linhas_por_linguagem.plot(kind="bar", figsize=(10, 6), title="Média de Linhas de Código por Linguagem")
plt.ylabel("Linhas de Código")
plt.xlabel("Linguagem")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("./bi/linhas_codigo_por_linguagem.png")
plt.clf()

