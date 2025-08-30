#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

# ---------------- knobs ----------------
export TIMEOUT_SEC="${TIMEOUT_SEC:-980}"       # limite por execução (s)
export SAMPLE_INTERVAL="${SAMPLE_INTERVAL:-0.001}"  # intervalo de amostragem do coletor
export MONITOR_MIN_S="${MONITOR_MIN_S:-0.006}"

LOG="${LOG:-run.log}"
OUT_JSON="${OUT_JSON:-resultados/metricas.json}"

# Filtros opcionais (listas separadas por vírgula, sem espaços)
# ex.: ONLY_CLASSES="p,np-completo"  ONLY_LANGS="c,python"  ONLY_SIZES="small,medium"
ONLY_CLASSES="${ONLY_CLASSES:-}"
ONLY_LANGS="${ONLY_LANGS:-}"
ONLY_SIZES="${ONLY_SIZES:-}"

# ---------------- helpers ----------------
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

# Normaliza filtros -> arrays (sem criar item vazio)
if [[ -n "$ONLY_CLASSES" ]]; then IFS=',' read -r -a ONLY_CLASSES_ARR <<< "$ONLY_CLASSES"; else ONLY_CLASSES_ARR=(); fi
if [[ -n "$ONLY_LANGS"   ]]; then IFS=',' read -r -a ONLY_LANGS_ARR   <<< "$ONLY_LANGS";   else ONLY_LANGS_ARR=();   fi
if [[ -n "$ONLY_SIZES"   ]]; then IFS=',' read -r -a ONLY_SIZES_ARR   <<< "$ONLY_SIZES";   else ONLY_SIZES_ARR=();   fi

in_filter() {
  # $1 valor; $2.. lista
  local val="$1"; shift
  [ "$#" -eq 0 ] && return 0           # sem filtro => permite
  local x
  for x in "$@"; do
    [[ "$val" == "$x" ]] && return 0
  done
  return 1
}

exists_in_json() {
  # Verifica se já há uma linha para (classe, linguagem, tamanho, repeticao, algoritmo_norm) no JSON
  # Uso: exists_in_json <classe> <ling> <tam> <rep> <algonorm>
  local classe="$1" ling="$2" tam="$3" rep="$4" alg="$5"
  [ -s "$OUT_JSON" ] || { echo 0; return; }
  python3 - "$OUT_JSON" "$classe" "$ling" "$tam" "$rep" "$alg" <<'PY'
import sys, json
p, classe, ling, tam, rep, alg = sys.argv[1:]
try:
    with open(p, 'r', encoding='utf-8') as f:
        data = json.load(f)
except Exception:
    print(0); sys.exit(0)

for row in data if isinstance(data, list) else []:
    try:
        if (str(row.get("classe")) == classe and
            str(row.get("linguagem")) == ling and
            str(row.get("tamanho")) == tam and
            int(row.get("repeticao")) == int(rep) and
            str(row.get("algoritmo_norm", row.get("algoritmo",""))) == alg):
            print(1); sys.exit(0)
    except Exception:
        pass
print(0)
PY
}

run_case() {
  # run_case <classe> <linguagem> <tamanho> <repeticao> <algonorm>
  local classe="$1" linguagem="$2" tamanho="$3" repeticao="$4" algonorm="$5"

  # filtros
  in_filter "$classe"    "${ONLY_CLASSES_ARR[@]}" || { echo "skip $classe (filtrado)"; return 0; }
  in_filter "$linguagem" "${ONLY_LANGS_ARR[@]}"   || { echo "skip $linguagem (filtrado)"; return 0; }
  in_filter "$tamanho"   "${ONLY_SIZES_ARR[@]}"   || { echo "skip $tamanho (filtrado)"; return 0; }

  # política: exato não roda em large (também checado dentro do coletor)
  if [[ "$classe" == "np-completo" && "$algonorm" == "exato" && "$tamanho" == "large" ]]; then
    echo "⏭️  skip np-completo(exato) em large (política)"
    return 0
  fi

  # retomar: já existe?
  if [[ "$(exists_in_json "$classe" "$linguagem" "$tamanho" "$repeticao" "$algonorm")" == "1" ]]; then
    echo "↩︎  já existe em $OUT_JSON → $classe | $linguagem | $tamanho | rep $repeticao | $algonorm"
    return 0
  fi

  echo "🧪 $classe($algonorm) | $linguagem | $tamanho | rep $repeticao" | tee -a "$LOG"

  # Monta env dinâmico pro coletor
  local -a cmd_env=(ALGO_VARIANT="$algonorm" SAMPLE_INTERVAL="$SAMPLE_INTERVAL" TIMEOUT_SEC="$TIMEOUT_SEC")
  if [[ -n "${MONITOR_MIN_S:-}" ]]; then cmd_env+=(MONITOR_MIN_S="$MONITOR_MIN_S"); fi

  local -a cmd=(env "${cmd_env[@]}" python3 coleta_metricas.py "$classe" "$linguagem" "$tamanho" "$repeticao")

  # Captura o exit code real do python mesmo com tee
  local rc
  set +e
  "${cmd[@]}" 2>&1 | tee -a "$LOG"
  rc=${PIPESTATUS[0]}
  set -e

  if [[ "$rc" -eq 0 ]]; then
    echo "✅ ok  $classe($algonorm) | $linguagem | $tamanho | rep $repeticao" | tee -a "$LOG"
  else
    echo "❌ fail rc=$rc  $classe($algonorm) | $linguagem | $tamanho | rep $repeticao" | tee -a "$LOG"
  fi

  return "$rc"
}

echo "== Run started at $(date) ==" | tee -a "$LOG"
echo "TIMEOUT_SEC=${TIMEOUT_SEC} USE_DOTNET=${USE_DOTNET} SAMPLE_INTERVAL=${SAMPLE_INTERVAL} MONITOR_MIN_S=${MONITOR_MIN_S:-}" | tee -a "$LOG"

classes=("np-dificil")   # adicione np, np-completo, np-dificil conforme necessário
linguagens=(c "c++" "c#" java go rust typescript javascript kotlin python)
tamanhos=(small medium large)

# toolchains
echo "toolchains: gcc=$need_gcc g++=$need_gpp rustc=$need_rustc go=$need_go java=$need_java kotlinc=$need_kotlin node=$need_node npx=$need_npx dotnet=$USE_DOTNET mono=$need_mono" | tee -a "$LOG"

for classe in "${classes[@]}"; do
  for linguagem in "${linguagens[@]}"; do
    # pular linguagem se toolchain ausente
    case "$linguagem" in
      c)          [ "$need_gcc"   -eq 1 ] || { echo "skip c (gcc missing)" | tee -a "$LOG"; continue; } ;;
      "c++")      [ "$need_gpp"   -eq 1 ] || { echo "skip c++ (g++ missing)" | tee -a "$LOG"; continue; } ;;
      "c#")
        if [ "${USE_DOTNET:-0}" -eq 1 ]; then
          have dotnet || { echo "skip c# (dotnet missing)" | tee -a "$LOG"; continue; }
        else
          [ "$need_mono" -eq 1 ] || { echo "skip c# (mono missing)" | tee -a "$LOG"; continue; }
        fi
        ;;
      java)       [ "$need_java"  -eq 1 ] || { echo "skip java (java/javac missing)" | tee -a "$LOG"; continue; } ;;
      go)         [ "$need_go"    -eq 1 ] || { echo "skip go (go missing)" | tee -a "$LOG"; continue; } ;;
      rust)       [ "$need_rustc" -eq 1 ] || { echo "skip rust (rustc missing)" | tee -a "$LOG"; continue; } ;;
      typescript) [ "$need_npx"   -eq 1 ] || { echo "skip typescript (npx/tsx missing)" | tee -a "$LOG"; continue; } ;;
      javascript) [ "$need_node"  -eq 1 ] || { echo "skip javascript (node missing)" | tee -a "$LOG"; continue; } ;;
      kotlin)     [ "$need_kotlin" -eq 1 ]|| { echo "skip kotlin (kotlinc missing)" | tee -a "$LOG"; continue; } ;;
      python)     have python3          || { echo "skip python (python3 missing)" | tee -a "$LOG"; continue; } ;;
    esac

    for tamanho in "${tamanhos[@]}"; do
      for repeticao in {1..30}; do
        if [[ "$classe" == "np-completo" ]]; then
          run_case "$classe" "$linguagem" "$tamanho" "$repeticao" "guloso"  || true
          if [[ "$tamanho" != "large" ]]; then
            run_case "$classe" "$linguagem" "$tamanho" "$repeticao" "exato" || true
          fi
        else
          # para as outras classes, algoritmo_norm é "exato" por padrão
          run_case "$classe" "$linguagem" "$tamanho" "$repeticao" "exato"   || true
        fi
      done
    done
  done
done

echo "== Run finished at $(date) ==" | tee -a "$LOG"
