#!/bin/bash

cd "$(dirname "$0")"

for classe in p np np-completo np-dificil; do
  for linguagem in "c" "c++" "c#" "go" "java" "javascript" "python" "typescript" "kotlin" "rust"; do
    for tamanho in small medium large; do
      for repeticao in {1..30}; do
        echo "🧪 Rodando $classe | $linguagem | $tamanho | Repetição $repeticao"
        python3 coleta_metricas.py "$classe" "$linguagem" "$tamanho" "$repeticao"
      done
    done
  done
done