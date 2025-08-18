#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

# ---- knobs
export TIMEOUT_SEC="${TIMEOUT_SEC:-180}"   # per-run timeout
LOG="${LOG:-run.log}"

have() { command -v "$1" >/dev/null 2>&1; }

# prefer dotnet for C# if available
if have dotnet; then export USE_DOTNET=1; else export USE_DOTNET=0; fi

# tool checks to avoid hard failures
need_go=$(have go && echo 1 || echo 0)
need_node=$(have node && echo 1 || echo 0)
need_tsx=$(have npx && npx --yes --package tsx --help >/dev/null 2>&1 && echo 1 || echo 0)
need_java=$(have java && have javac && echo 1 || echo 0)
need_kotlin=$(have kotlinc && echo 1 || echo 0)
need_gcc=$(have gcc && echo 1 || echo 0)
need_gpp=$(have g++ && echo 1 || echo 0)
need_rustc=$(have rustc && echo 1 || echo 0)
need_mono=$(have mono && echo 1 || echo 0)

echo "== Run started at $(date) ==" | tee -a "$LOG"

for classe in p; do
  for linguagem in c "c++" "c#" java go rust typescript javascript kotlin python; do

    # skip if runtime/compiler missing
    case "$linguagem" in
      c)         [ "$need_gcc" -eq 1 ]      || { echo "skip c (gcc missing)"; continue; } ;;
      "c++")     [ "$need_gpp" -eq 1 ]      || { echo "skip c++ (g++ missing)"; continue; } ;;
      "c#")      if [ "${USE_DOTNET:-0}" -eq 1 ]; then have dotnet || { echo "skip c# (dotnet missing)"; continue; }
                 else [ "$need_mono" -eq 1 ] || { echo "skip c# (mono missing)"; continue; }; fi ;;
      java)      [ "$need_java" -eq 1 ]     || { echo "skip java (java/javac missing)"; continue; } ;;
      go)        [ "$need_go" -eq 1 ]       || { echo "skip go (go missing)"; continue; } ;;
      rust)      [ "$need_rustc" -eq 1 ]    || { echo "skip rust (rustc missing)"; continue; } ;;
      typescript)[ "$need_tsx" -eq 1 ]      || { echo "skip ts (tsx missing)"; continue; } ;;
      javascript)[ "$need_node" -eq 1 ]     || { echo "skip js (node missing)"; continue; } ;;
      kotlin)    [ "$need_kotlin" -eq 1 ]   || { echo "skip kotlin (kotlinc missing)"; continue; } ;;
      python)    have python3                || { echo "skip python (python3 missing)"; continue; } ;;
    esac

    for tamanho in small medium large; do
      for repeticao in {1..30}; do
        echo "🧪 $classe | $linguagem | $tamanho | rep $repeticao" | tee -a "$LOG"
        python3 coleta_metricas.py "$classe" "$linguagem" "$tamanho" "$repeticao" | tee -a "$LOG"
      done
    done
  done
done

echo "== Run finished at $(date) ==" | tee -a "$LOG"
