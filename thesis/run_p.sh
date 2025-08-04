#!/bin/bash

cd "$(dirname "$0")"

for classe in p; do
  for linguagem in "c" "c++" "c#" "java" "go" "rust" "typescript" "javascript" "kotlin" "python"; do
    for tamanho in small medium large; do
      for repeticao in {1..2}; do
        echo "🧪 Rodando $classe | $linguagem | $tamanho | Repetição $repeticao"
        python3 coleta_metricas.py "$classe" "$linguagem" "$tamanho" "$repeticao"
      done
    done
  done
done