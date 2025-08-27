#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, psutil, time, subprocess, sys, json, platform, threading, shutil, re, unicodedata
from datetime import datetime
import distro
import resource  # POSIX: tempos de CPU com melhor resolução para jobs curtos
from pathlib import Path

# ===================== Args =====================
if len(sys.argv) != 5:
    print("Uso: python3 coleta_metricas.py <classe> <linguagem> <tamanho> <repeticao>")
    sys.exit(2)

classe, linguagem, tamanho, repeticao = sys.argv[1:]
ling = linguagem.lower()

# ===================== Variantes (np-completo) =====================
algoritmo_variant = os.environ.get("ALGO_VARIANT", "").strip().lower()
if classe == "np-completo":
    if algoritmo_variant not in {"exato", "guloso"}:
        algoritmo_variant = "exato"
else:
    algoritmo_variant = "exato"

def _is_large_bucket(name: str) -> bool:
    s = str(name).strip().lower()
    return s in {"large", "grande"}

if classe == "np-completo" and algoritmo_variant == "exato" and _is_large_bucket(tamanho):
    print("⏭️  Skip: NP-completo (exato) não roda em 'large' por política de testes.")
    sys.exit(0)

# ===================== Mapeamentos =====================
problema_por_classe = {
    "p": "mergesort",
    "np": "factoring",
    "np-completo": "knapsack",
    "np-dificil": "halting",
}
if classe == "np-completo":
    problema_padrao = problema_por_classe["np-completo"]
    algoritmo_padrao = algoritmo_variant or "exato"
else:
    problema_padrao = problema_por_classe.get(classe)
    algoritmo_padrao = "exato"

algoritmo_norm = "guloso" if (classe == "np-completo" and algoritmo_padrao.lower().startswith("gulo")) else "exato"

# ===================== Paths =====================
base_dir = os.path.dirname(os.path.abspath(__file__))
BIN_DIR   = os.path.join(base_dir, "bin", ling)
OUT_DIR   = os.path.join(base_dir, "resultados")
os.makedirs(BIN_DIR, exist_ok=True)
os.makedirs(OUT_DIR, exist_ok=True)

arquivo_por_classe = {"p": "p", "np": "np", "np-completo": "np-completo", "np-dificil": "np-dificil"}
dataset_por_classe = {"p": "merge_sort.json", "np": "factoring.json", "np-completo": "knapsack.json", "np-dificil": "halting.json"}
ext_map = {"c":"c","c++":"cpp","c#":"cs","go":"go","java":"java","javascript":"js","python":"py","typescript":"ts","kotlin":"kt","rust":"rs"}

if ling not in ext_map:
    print(f"❌ Linguagem não suportada: {ling}")
    sys.exit(2)

extensao = ext_map[ling]
nome_arquivo_base = arquivo_por_classe[classe]

# nomes por linguagem
nome_classe_java = None
if ling == "java":
    if classe == "np-completo" and algoritmo_variant:
        nome_classe_java = "NpCompletoExato" if algoritmo_variant == "exato" else "NpCompletoGuloso"
        nome_arquivo = f"{nome_classe_java}.java"
    else:
        nome_classe_java = ''.join(part.capitalize() for part in nome_arquivo_base.replace('-', ' ').split())
        nome_arquivo = f"{nome_classe_java}.java"
else:
    if classe == "np-completo" and algoritmo_variant:
        nome_arquivo_base = f"{nome_arquivo_base}_{algoritmo_variant}"
    nome_arquivo = f"{nome_arquivo_base}.{extensao}"

alg_path = os.path.join(base_dir, "algorithms", ling, nome_arquivo)
dataset_nome = dataset_por_classe[classe]
dataset_path = os.path.join(base_dir, "datasets", tamanho, dataset_nome)

if not os.path.exists(alg_path):
    print(f"❌ Arquivo de algoritmo não encontrado: {alg_path}")
    sys.exit(1)
if not os.path.exists(dataset_path):
    print(f"❌ Dataset não encontrado: {dataset_path}")
    sys.exit(1)

dataset_id = os.path.splitext(os.path.basename(dataset_path))[0]
instancia = f"{dataset_id}:{tamanho}"

# ===================== Specs =====================
specs = {
    "sistema_operacional": platform.system(),
    "distro": distro.name(pretty=True),
    "versao_os": distro.version(pretty=True),
    "kernel": platform.release(),
    "arquitetura": platform.machine(),
    "cpu_modelo": platform.processor(),
    "cpu_cores": psutil.cpu_count(logical=True),
    "memoria_total_mb": round(psutil.virtual_memory().total / (1024 ** 2), 2),
}
N_CORES = max(1, specs["cpu_cores"])

# ===================== Knobs =====================
SCHEMA_VERSION  = 2
SAMPLE_INTERVAL = float(os.environ.get("SAMPLE_INTERVAL", "0.02"))
TIMEOUT_SEC     = int(os.environ.get("TIMEOUT_SEC", "580"))
SAMPLES_HZ      = (1.0 / SAMPLE_INTERVAL) if SAMPLE_INTERVAL > 0 else 0.0
MONITOR_MIN_S   = float(os.environ.get("MONITOR_MIN_S", "0"))
MIN_SAMPLES     = int(os.environ.get("MIN_SAMPLES", "3"))           # garante janela mínima em amostras
WARMUP_SPIN_S   = float(os.environ.get("WARMUP_SPIN_S", "0.003"))   # spinning curtíssimo p/ capturar 1ª amostra

# ===================== Helpers =====================
def which(cmd: str) -> bool:
    return shutil.which(cmd) is not None

def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)

def prime_cpu_counters(proc: psutil.Process):
    try:
        procs = [proc] + proc.children(recursive=True)
        for p in procs:
            try:
                p.cpu_percent(0.0)
            except psutil.NoSuchProcess:
                pass
    except psutil.NoSuchProcess:
        pass

def _deaccent_lower(s: str) -> str:
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn').lower()

def extrai_valor_objetivo(stdout_text: str, stderr_text: str = ""):
    for text in (stdout_text, stderr_text):
        if not text:
            continue
        ntext = _deaccent_lower(text)
        m = re.search(r'"valor_objetivo"\s*:\s*(\d+)', ntext, flags=re.IGNORECASE)
        if m:
            try: return int(m.group(1))
            except: pass
        m = re.search(r'valor[_\s]*objetivo\s*:\s*(\d+)', ntext, flags=re.IGNORECASE)
        if m:
            try: return int(m.group(1))
            except: pass
        candidates = []
        for line in ntext.splitlines():
            m = re.search(r'(valor|value)[^\d]{0,30}(\d+)', line)
            if m:
                try: candidates.append(int(m.group(2))); continue
                except: pass
            if ("valor" in line or "value" in line):
                nums = re.findall(r'(\d+)', line)
                if nums:
                    try: candidates.append(int(nums[-1]))
                    except: pass
        if candidates:
            return candidates[-1]
    return None

# ===================== Compilação =====================
compile_ok = True
compile_stdout = ""
compile_stderr = ""

exe_path = os.path.join(BIN_DIR, "exe")
jar_path = os.path.join(BIN_DIR, "main.jar")
USE_DOTNET = os.environ.get("USE_DOTNET", "0") == "1"

compilacoes = {
    "c":      ["gcc", alg_path, "-O2", "-o", exe_path, "-lm"],
    "c++":    ["g++", alg_path, "-O2", "-o", exe_path],
    "java":   ["javac", alg_path, "-d", BIN_DIR],
    "kotlin": ["kotlinc", alg_path, "-include-runtime", "-d", jar_path],
    "rust":   ["rustc", "-C", "opt-level=3", alg_path, "-o", exe_path],
}

def compile_csharp_dotnet():
    if not which("dotnet"): return False, "", "dotnet não encontrado no PATH"
    proj_dir = os.path.join(BIN_DIR, "csharp_proj")
    os.makedirs(proj_dir, exist_ok=True)
    csproj = os.path.join(proj_dir, "Program.csproj")
    with open(csproj, "w", encoding="utf-8") as f:
        f.write(f"""<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <Optimize>true</Optimize>
    <AssemblyName>Program</AssemblyName>
  </PropertyGroup>
  <ItemGroup>
    <Compile Include="{alg_path}" Link="Program.cs" />
  </ItemGroup>
</Project>
""")
    r = run(["dotnet", "build", proj_dir, "-c", "Release", "-o", BIN_DIR])
    return r.returncode == 0, r.stdout, r.stderr

def compile_csharp_mono():
    if not which("mcs"): return False, "", "mcs/mono não encontrado no PATH"
    r = run(["mcs", alg_path, "-out:" + os.path.join(BIN_DIR, "exe.exe")])
    return r.returncode == 0, r.stdout, r.stderr

if ling in compilacoes:
    if not which(compilacoes[ling][0]):
        compile_ok = False; compile_stderr = f"Compilador '{compilacoes[ling][0]}' não encontrado."
    else:
        r = run(compilacoes[ling]); compile_ok = (r.returncode == 0); compile_stdout, compile_stderr = r.stdout, r.stderr
elif ling == "c#":
    if USE_DOTNET: compile_ok, compile_stdout, compile_stderr = compile_csharp_dotnet()
    else:          compile_ok, compile_stdout, compile_stderr = compile_csharp_mono()

def persist_compile_error_and_exit(stdout_msg: str, stderr_msg: str):
    idle_cpu = psutil.cpu_percent(interval=1)
    idle_ram = psutil.virtual_memory().used / (1024 ** 2)
    linhas_codigo = sum(1 for _ in open(alg_path, 'r', encoding="utf-8", errors="ignore"))
    result = {
        "schema_version": SCHEMA_VERSION, "monitor_interval_s": SAMPLE_INTERVAL, "samples_hz": SAMPLES_HZ,
        "classe": classe, "problema": problema_padrao, "algoritmo": algoritmo_padrao, "algoritmo_norm": algoritmo_norm,
        "linguagem": linguagem, "tamanho": tamanho, "instancia": instancia, "dataset_id": dataset_id,
        "repeticao": int(repeticao), "tempo_s": 0.0, "cpu_before": idle_cpu, "ram_before_mb": round(idle_ram, 2),
        "cpu_avg_during": 0.0, "cpu_max_during": 0.0, "cpu_avg_during_norm": 0.0, "cpu_max_during_norm": 0.0,
        "ram_avg_during_mb": 0.0, "ram_max_during_mb": 0.0, "ram_peak_mb": 0.0,
        "cpu_time_user_s": 0.0, "cpu_time_system_s": 0.0, "cpu_time_total_s": 0.0, "cpu_util_norm_pct_time": 0.0,
        "wall_time_s": 0.0, "cpu_after": 0.0, "ram_after_mb": round(psutil.virtual_memory().used / (1024 ** 2), 2),
        "linhas_codigo": linhas_codigo, "timestamp": datetime.now().isoformat(), "especificacoes_sistema": specs,
        "stdout": stdout_msg, "stderr": stderr_msg, "exit_code": -1, "timeout_s": 0, "samples": 0, "valor_objetivo": None,
    }
    err_file = os.path.join(OUT_DIR, "erro.json")
    try:
        all_results = json.load(open(err_file, encoding="utf-8")) if os.path.exists(err_file) and os.path.getsize(err_file) > 0 else []
    except Exception:
        all_results = []
    all_results.append(result)
    with open(err_file, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    print("❌ Erro na compilação. Resultado salvo.")
    sys.exit(1)

if not compile_ok:
    persist_compile_error_and_exit(compile_stdout, compile_stderr)

# ===================== Execução =====================
execucoes = {
    "c":          [exe_path, tamanho],
    "c++":        [exe_path, tamanho],
    "rust":       [exe_path, tamanho],
    "go":         ["go", "run", alg_path, tamanho],
    "java":       ["java", "-cp", BIN_DIR, nome_classe_java, tamanho] if nome_classe_java else None,
    "kotlin":     ["java", "-jar", jar_path, tamanho],
    "javascript": ["node", alg_path, tamanho],
    "typescript": ["npx", "tsx", alg_path, tamanho],
    "python":     ["python3", alg_path, tamanho],
}
if ling == "c#":
    if USE_DOTNET:
        execucoes["c#"] = ["dotnet", os.path.join(BIN_DIR, "Program.dll"), tamanho]
    else:
        execucoes["c#"] = ["mono", os.path.join(BIN_DIR, "exe.exe"), tamanho]

if ling not in execucoes or execucoes[ling] is None:
    print(f"❌ Sem comando de execução para {ling}")
    sys.exit(2)

first_exe = execucoes[ling][0]
def _which_or_isfile(x): return os.path.isfile(x) or which(x)
if not _which_or_isfile(first_exe):
    print(f"❌ Runtime/ferramenta não encontrada: {first_exe}")
    sys.exit(1)

idle_cpu = psutil.cpu_percent(interval=0.8)
idle_ram = psutil.virtual_memory().used / (1024 ** 2)

with open(alg_path, 'r', encoding="utf-8", errors="ignore") as code_file:
    linhas_codigo = sum(1 for _ in code_file)

metrics = []    # (cpu_total_pct, ram_peak_inst_mb)
timeout_hit = False
exit_code = None
state = {"cpu_user": 0.0, "cpu_sys": 0.0, "ram_peak": 0.0}

def _ru_maxrss_to_mb(ru) -> float:
    rss = float(getattr(ru, "ru_maxrss", 0) or 0.0)
    if rss <= 0: return 0.0
    return rss / 1024.0 if rss <= 10_000_000 else rss / (1024.0 ** 2)

def monitor_process(proc):
    """Amostra CPU/RAM garantindo janela mínima e lidando com processos curtíssimos."""
    last_cpu_times = {}
    t0 = time.perf_counter()
    try:
        # Se o processo já terminou antes do monitor subir, apenas retorne silenciosamente
        try:
            parent = psutil.Process(proc.pid)
        except psutil.NoSuchProcess:
            return

        prime_cpu_counters(parent)

        while True:
            alive = (proc.poll() is None)
            cpu_total_pct = 0.0
            ram_peak_inst = 0.0

            try:
                procs = [parent] + parent.children(recursive=True) if alive else []
            except psutil.NoSuchProcess:
                procs = []
                alive = False

            seen_pids = set()
            for p in procs:
                try:
                    u, s = p.cpu_times().user, p.cpu_times().system
                    pid = p.pid
                    seen_pids.add(pid)
                    if pid in last_cpu_times:
                        lu, ls = last_cpu_times[pid]
                        state["cpu_user"] += max(0.0, u - lu)
                        state["cpu_sys"]  += max(0.0, s - ls)
                    last_cpu_times[pid] = (u, s)

                    rss_mb = p.memory_info().rss / (1024 ** 2)
                    ram_peak_inst = max(ram_peak_inst, rss_mb)
                    cpu_total_pct += p.cpu_percent(0.0)
                except psutil.NoSuchProcess:
                    continue
                except Exception:
                    continue

            for pid in list(last_cpu_times.keys()):
                if pid not in seen_pids:
                    last_cpu_times.pop(pid, None)

            metrics.append((cpu_total_pct, ram_peak_inst))
            if ram_peak_inst > state["ram_peak"]:
                state["ram_peak"] = ram_peak_inst

            elapsed = time.perf_counter() - t0
            need_time = MONITOR_MIN_S
            need_samples = max(0, MIN_SAMPLES - len(metrics)) * SAMPLE_INTERVAL
            min_window = max(need_time, need_samples)

            if (not alive) and (elapsed >= min_window):
                break

            time.sleep(SAMPLE_INTERVAL)
    except Exception as e:
        # Só loga se pedir explicitamente (evita ruído no fast-path)
        if os.environ.get("DEBUG_MONITOR") == "1":
            print(f"[monitor] aviso: {e}")

exec_cmd = execucoes[ling]
ru_before = resource.getrusage(resource.RUSAGE_CHILDREN)

start = time.time()
proc = subprocess.Popen(exec_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# -------- Warm-up síncrono: tenta capturar 1 amostra viva imediatamente --------
t0_warm = time.perf_counter()
rss0 = None
while (time.perf_counter() - t0_warm) < WARMUP_SPIN_S:
    try:
        p = psutil.Process(proc.pid)
        p.cpu_percent(0.0)  # prime
        rss0 = p.memory_info().rss / (1024 ** 2)
        break
    except psutil.NoSuchProcess:
        time.sleep(min(0.0005, SAMPLE_INTERVAL / 10.0))
    except Exception:
        break
if rss0 is not None:
    metrics.append((0.0, rss0))
    state["ram_peak"] = max(state["ram_peak"], rss0)

monitor_thread = threading.Thread(target=monitor_process, args=(proc,), daemon=True)
monitor_thread.start()

try:
    stdout, stderr = proc.communicate(timeout=TIMEOUT_SEC)
    exit_code = proc.returncode
except subprocess.TimeoutExpired:
    timeout_hit = True
    proc.kill()
    try:
        stdout, stderr = proc.communicate(timeout=5)
    except Exception:
        stdout, stderr = b"", b""
finally:
    monitor_thread.join(timeout=2)

end = time.time()
wall_time = end - start

# garante ao menos 1 amostra (evita séries vazias)
if len(metrics) == 0:
    metrics.append((0.0, 0.0))

cpu_series = [m[0] for m in metrics]
ram_series = [m[1] for m in metrics]
def mean(xs): return round(sum(xs)/len(xs), 2) if xs else 0.0
cpu_avg = mean(cpu_series)
cpu_max = round(max(cpu_series), 2) if cpu_series else 0.0
ram_avg = mean(ram_series)
ram_max = round(max(ram_series), 2) if ram_series else 0.0
cpu_avg_norm = round(cpu_avg / N_CORES, 2)
cpu_max_norm = round(cpu_max / N_CORES, 2)

cpu_after = psutil.cpu_percent(interval=0.5)
ram_after = psutil.virtual_memory().used / (1024 ** 2)

stdout_text = stdout.decode(errors="replace")
stderr_text = stderr.decode(errors="replace")
valor_obj = None
if classe == "np-completo" and problema_padrao == "knapsack":
    valor_obj = extrai_valor_objetivo(stdout_text, stderr_text)

cpu_time_user = float(state["cpu_user"])
cpu_time_sys  = float(state["cpu_sys"])
cpu_time_total = cpu_time_user + cpu_time_sys

ru_after = resource.getrusage(resource.RUSAGE_CHILDREN)
u_fallback = max(0.0, ru_after.ru_utime - ru_before.ru_utime)
s_fallback = max(0.0, ru_after.ru_stime - ru_before.ru_stime)
if (cpu_time_total == 0.0) and ((u_fallback + s_fallback) > 0.0):
    cpu_time_user = u_fallback
    cpu_time_sys  = s_fallback
    cpu_time_total = cpu_time_user + cpu_time_sys

ru_peak_mb_before = _ru_maxrss_to_mb(ru_before)
ru_peak_mb_after  = _ru_maxrss_to_mb(ru_after)
ru_peak_delta_mb  = max(0.0, ru_peak_mb_after - ru_peak_mb_before)
if state["ram_peak"] <= 0.0 and ru_peak_delta_mb > 0.0:
    state["ram_peak"] = ru_peak_delta_mb
elif ru_peak_delta_mb > 0.0:
    state["ram_peak"] = max(state["ram_peak"], ru_peak_delta_mb)

cpu_util_norm_pct_time = round((cpu_time_total / wall_time) / N_CORES * 100.0, 2) if wall_time > 0 else 0.0

result = {
    "schema_version": SCHEMA_VERSION,
    "monitor_interval_s": SAMPLE_INTERVAL,
    "samples_hz": SAMPLES_HZ,
    "classe": classe,
    "problema": problema_padrao,
    "algoritmo": algoritmo_padrao,
    "algoritmo_norm": algoritmo_norm,
    "linguagem": linguagem,
    "tamanho": tamanho,
    "instancia": instancia,
    "dataset_id": dataset_id,
    "repeticao": int(repeticao),
    "tempo_s": round(wall_time, 6),
    "cpu_before": idle_cpu,
    "ram_before_mb": round(idle_ram, 2),
    "cpu_avg_during": cpu_avg,
    "cpu_max_during": cpu_max,
    "cpu_avg_during_norm": cpu_avg_norm,
    "cpu_max_during_norm": cpu_max_norm,
    "ram_avg_during_mb": ram_avg,
    "ram_max_during_mb": ram_max,
    "ram_peak_mb": round(state["ram_peak"], 2),
    "cpu_time_user_s": round(cpu_time_user, 6),
    "cpu_time_system_s": round(cpu_time_sys, 6),
    "cpu_time_total_s": round(cpu_time_total, 6),
    "cpu_util_norm_pct_time": cpu_util_norm_pct_time,
    "wall_time_s": round(wall_time, 6),
    "cpu_after": cpu_after,
    "ram_after_mb": round(ram_after, 2),
    "linhas_codigo": linhas_codigo,
    "timestamp": datetime.now().isoformat(),
    "especificacoes_sistema": specs,
    "stdout": stdout_text,
    "stderr": stderr_text,
    "exit_code": exit_code if exit_code is not None else -1,
    "timeout_s": TIMEOUT_SEC if timeout_hit else 0,
    "samples": len(metrics),
    "valor_objetivo": valor_obj,
}

# ===================== Saída JSON (suporta OUT_JSON) =====================
out_json_env = os.environ.get("OUT_JSON", "").strip()
if out_json_env:
    output_file = Path(out_json_env)
    if not output_file.is_absolute():
        output_file = Path(base_dir) / output_file
else:
    output_file = Path(OUT_DIR) / "metricas.json"

output_file.parent.mkdir(parents=True, exist_ok=True)

try:
    if output_file.exists() and output_file.stat().st_size > 0:
        with output_file.open("r", encoding="utf-8") as f:
            all_results = json.load(f)
    else:
        all_results = []
except Exception:
    all_results = []

all_results.append(result)
with output_file.open("w", encoding="utf-8") as f:
    json.dump(all_results, f, indent=2, ensure_ascii=False)

print(f"✅ Finalizado e adicionado em: {output_file.name}")
