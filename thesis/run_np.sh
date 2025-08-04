#!/bin/bash

cd "$(dirname "$0")"

for classe in np; do
  for linguagem in "typescript" "c++" "c#" "java" "go" "rust" "typescript" "javascript" "kotlin" "python"; do
    for tamanho in small medium large; do
      for repeticao in {1..30}; do
        echo "🧪 Rodando $classe | $linguagem | $tamanho | Repetição $repeticao"
        python3 coleta_metricas.py "$classe" "$linguagem" "$tamanho" "$repeticao"
      done
    done
  done
done