#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

# ---------- knobs ----------
export TIMEOUT_SEC="${TIMEOUT_SEC:-180}"   # tempo limite por execução (s)
LOG="${LOG:-run.log}"

# ---------- helpers ----------
have() { command -v "$1" >/dev/null 2>&1; }

# Preferir .NET para C# quando disponível
if have dotnet; then export USE_DOTNET=1; else export USE_DOTNET=0; fi

# Checagens de toolchain (uma vez)
need_go=$(have go && echo 1 || echo 0)
need_node=$(have node && echo 1 || echo 0)
need_java=$(( $(have java && echo 1 || echo 0) * $(have javac && echo 1 || echo 0) ))
need_kotlin=$(have kotlinc && echo 1 || echo 0)
need_gcc=$(have gcc && echo 1 || echo 0)
need_gpp=$(have g++ && echo 1 || echo 0)
need_rustc=$(have rustc && echo 1 || echo 0)
need_mono=$(have mono && echo 1 || echo 0)
need_npx=$(have npx && echo 1 || echo 0)  # para tsx

echo "== Run started at $(date) ==" | tee -a "$LOG"
echo "TIMEOUT_SEC=${TIMEOUT_SEC} USE_DOTNET=${USE_DOTNET}" | tee -a "$LOG"

classes=(np)
linguagens=(c "c++" "c#" java go rust typescript javascript kotlin python)
tamanhos=(small medium large)

for classe in "${classes[@]}"; do
  for linguagem in "${linguagens[@]}"; do
    # pular linguagem se toolchain ausente
    case "$linguagem" in
      c)         [ "$need_gcc" -eq 1 ]      || { echo "skip c (gcc missing)" | tee -a "$LOG"; continue; } ;;
      "c++")     [ "$need_gpp" -eq 1 ]      || { echo "skip c++ (g++ missing)" | tee -a "$LOG"; continue; } ;;
      "c#")
        if [ "${USE_DOTNET:-0}" -eq 1 ]; then
          have dotnet || { echo "skip c# (dotnet missing)" | tee -a "$LOG"; continue; }
        else
          [ "$need_mono" -eq 1 ] || { echo "skip c# (mono missing)" | tee -a "$LOG"; continue; }
        fi
        ;;
      java)      [ "$need_java" -eq 1 ]     || { echo "skip java (java/javac missing)" | tee -a "$LOG"; continue; } ;;
      go)        [ "$need_go" -eq 1 ]       || { echo "skip go (go missing)" | tee -a "$LOG"; continue; } ;;
      rust)      [ "$need_rustc" -eq 1 ]    || { echo "skip rust (rustc missing)" | tee -a "$LOG"; continue; } ;;
      typescript)[ "$need_npx" -eq 1 ]      || { echo "skip typescript (npx/tsx missing)" | tee -a "$LOG"; continue; } ;;
      javascript)[ "$need_node" -eq 1 ]     || { echo "skip javascript (node missing)" | tee -a "$LOG"; continue; } ;;
      kotlin)    [ "$need_kotlin" -eq 1 ]   || { echo "skip kotlin (kotlinc missing)" | tee -a "$LOG"; continue; } ;;
      python)    have python3                || { echo "skip python (python3 missing)" | tee -a "$LOG"; continue; } ;;
    esac

    for tamanho in "${tamanhos[@]}"; do
      for repeticao in {1..30}; do
        if [[ "$classe" == "np-completo" ]]; then
          # 1) Guloso: sempre
          echo "🧪 $classe(guloso) | $linguagem | $tamanho | rep $repeticao" | tee -a "$LOG"
          ALGO_VARIANT="guloso" \
          python3 coleta_metricas.py "$classe" "$linguagem" "$tamanho" "$repeticao" | tee -a "$LOG"

          # 2) Exato: somente small/medium
          if [[ "$tamanho" != "large" ]]; then
            echo "🧪 $classe(exato) | $linguagem | $tamanho | rep $repeticao" | tee -a "$LOG"
            ALGO_VARIANT="exato" \
            python3 coleta_metricas.py "$classe" "$linguagem" "$tamanho" "$repeticao" | tee -a "$LOG"
          fi
        else
          echo "🧪 $classe | $linguagem | $tamanho | rep $repeticao" | tee -a "$LOG"
          python3 coleta_metricas.py "$classe" "$linguagem" "$tamanho" "$repeticao" | tee -a "$LOG"
        fi
      done
    done
  done
done

echo "== Run finished at $(date) ==" | tee -a "$LOG"
