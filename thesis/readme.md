# TCC - Avaliação Comparativa de Algoritmos em Diferentes Linguagens de Programação

Este repositório contém o código-fonte e os scripts para execução dos experimentos do TCC.  
O objetivo é avaliar o desempenho de algoritmos clássicos implementados em diversas linguagens, coletando métricas como tempo de execução, uso de CPU, uso de memória e complexidade de implementação.  

---

## 🔧 Pré-requisitos

Certifique-se de estar utilizando **Ubuntu 22.04 LTS** ou superior.  

### 1. Atualizar pacotes e instalar compiladores / runtimes

Execute no terminal:

```bash
sudo apt update && sudo apt install -y   build-essential   gcc g++   mono-complete   openjdk-17-jdk   python3 python3-pip   nodejs npm   golang   rustc   default-jdk   curl unzip
```

### 2. Instalar bibliotecas Python necessárias

```bash
pip install -r requirements.txt
```

Ou, se preferir, copie e cole diretamente os requisitos abaixo:

```txt
psutil
matplotlib
pandas
distro
```

---

## ▶️ Execução do experimento

### 1. Rodar todos os algoritmos

O script `run_all.sh` executa todos os algoritmos em todas as linguagens, coletando métricas automaticamente.

```bash
chmod +x run_all.sh
./run_all.sh
```

Isso irá gerar os resultados em:

```
resultados/metricas.json
```

Esse arquivo JSON contém todas as métricas coletadas (tempo, CPU, memória, etc.) em formato estruturado.

---

## 📊 Geração de gráficos

Após a coleta dos dados, use o script `bi.py` para processar os resultados e gerar os gráficos.

```bash
python3 bi.py
```

Os gráficos serão gerados como arquivos **CSV + imagens** dentro da pasta:

```
bi/
```

- Cada métrica terá um arquivo CSV correspondente.  
- As imagens estarão em **PNG**, prontas para uso em relatórios e artigos.

---

## 📂 Estrutura do Projeto

```
.
├── algorithms/         # Implementações em diferentes linguagens
├── resultados/         # Saída dos experimentos (metricas.json)
├── bi/           # CSVs e PNGs dos gráficos gerados
├── run_all.sh          # Script de execução completa dos experimentos
├── coleta_metricas.py  # Script para rodar um experimento individual
├── bi.py               # Script de BI para gerar gráficos
└── README.md           # Este guia
```

---

## 🚀 Exemplo rápido

1. Executar todos os experimentos:  
   ```bash
   ./run_all.sh
   ```

2. Gerar gráficos:  
   ```bash
   python3 bi.py
   ```

3. Ver os resultados:  
   - Arquivo de métricas: `resultados/metricas.json`  
   - Gráficos e CSVs: pasta `bi/`

---