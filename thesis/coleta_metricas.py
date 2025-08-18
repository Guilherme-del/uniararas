#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, psutil, time, subprocess, sys, json, platform, threading, shutil
from datetime import datetime
import distro

# ===================== Args =====================
if len(sys.argv) != 5:
    print("Uso: python3 coleta_metricas.py <classe> <linguagem> <tamanho> <repeticao>")
    sys.exit(2)

classe, linguagem, tamanho, repeticao = sys.argv[1:]
ling = linguagem.lower()

# ===================== Variantes (np-completo) =====================
# Define algoritmo_variant via variável de ambiente (não quebra os 4 args)
algoritmo_variant = os.environ.get("ALGO_VARIANT", "").strip().lower()
if classe == "np-completo":
    if algoritmo_variant not in {"exato", "guloso"}:
        algoritmo_variant = "exato"  # default seguro
else:
    algoritmo_variant = ""  # vazio para as outras classes

def _is_large_bucket(name: str) -> bool:
    s = str(name).strip().lower()
    return s in {"large", "grande"}

# Regra: exato NÃO roda em large (skip elegante)
if classe == "np-completo" and algoritmo_variant == "exato" and _is_large_bucket(tamanho):
    print("⏭️  Skip: NP-completo (exato) não roda em 'large' por política de testes.")
    sys.exit(0)

# ===================== Const / Paths =====================
base_dir = os.path.dirname(os.path.abspath(__file__))
BIN_DIR   = os.path.join(base_dir, "bin", ling)         # bin por linguagem
OUT_DIR   = os.path.join(base_dir, "resultados")
os.makedirs(BIN_DIR, exist_ok=True)
os.makedirs(OUT_DIR, exist_ok=True)

arquivo_por_classe = {
    "p": "p",
    "np": "np",
    "np-completo": "np-completo",
    "np-dificil": "np-dificil",
}
dataset_por_classe = {
    "p": "merge_sort.json",
    "np": "factoring.json",
    "np-completo": "knapsack.json",
    "np-dificil": "halting.json",
}
ext_map = {
    "c": "c", "c++": "cpp", "c#": "cs", "go": "go", "java": "java",
    "javascript": "js", "python": "py", "typescript": "ts",
    "kotlin": "kt", "rust": "rs",
}
if ling not in ext_map:
    print(f"❌ Linguagem não suportada: {ling}")
    sys.exit(2)

extensao = ext_map[ling]
nome_arquivo_base = arquivo_por_classe[classe]

# Se for NP-completo, escolha base pelo algoritmo_variant
if classe == "np-completo" and algoritmo_variant:
    nome_arquivo_base = f"{nome_arquivo_base}_{algoritmo_variant}"

# Classe Java precisa ser nomeada corretamente
nome_classe_java = None
if ling == "java":
    nome_classe_java = ''.join(part.capitalize() for part in nome_arquivo_base.replace('-', ' ').split())
    nome_arquivo = f"{nome_classe_java}.java"
else:
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

# ===================== Especificações do sistema =====================
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

# ===================== Helpers =====================
def which(cmd: str) -> bool:
    return shutil.which(cmd) is not None

def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)

def prime_cpu_counters(proc: psutil.Process):
    """Faz leitura inicial para evitar primeira amostra 0%."""
    try:
        procs = [proc] + proc.children(recursive=True)
        for p in procs:
            try:
                p.cpu_percent(0.0)
            except psutil.NoSuchProcess:
                pass
    except psutil.NoSuchProcess:
        pass

# ===================== Compilação =====================
compile_ok = True
compile_stdout = ""
compile_stderr = ""

exe_path = os.path.join(BIN_DIR, "exe")
jar_path = os.path.join(BIN_DIR, "main.jar")

# C# com dotnet (preferido) ou mono (fallback)
USE_DOTNET = os.environ.get("USE_DOTNET", "0") == "1"

compilacoes = {
    "c":      ["gcc", alg_path, "-O2", "-o", exe_path, "-lm"],
    "c++":    ["g++", alg_path, "-O2", "-o", exe_path],
    "java":   ["javac", alg_path, "-d", BIN_DIR],
    "kotlin": ["kotlinc", alg_path, "-include-runtime", "-d", jar_path],
    "rust":   ["rustc", "-C", "opt-level=3", alg_path, "-o", exe_path],
}

def compile_csharp_dotnet():
    if not which("dotnet"):
        return False, "", "dotnet não encontrado no PATH"
    # csproj mínimo apontando para o arquivo fonte original
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
    if not which("mcs"):
        return False, "", "mcs/mono não encontrado no PATH"
    r = run(["mcs", alg_path, "-out:" + os.path.join(BIN_DIR, "exe.exe")])
    return r.returncode == 0, r.stdout, r.stderr

# Executa compilação quando necessário
if ling in compilacoes:
    if not which(compilacoes[ling][0]):
        compile_ok = False
        compile_stderr = f"Compilador '{compilacoes[ling][0]}' não encontrado."
    else:
        r = run(compilacoes[ling])
        compile_ok = (r.returncode == 0)
        compile_stdout, compile_stderr = r.stdout, r.stderr
elif ling == "c#":
    if USE_DOTNET:
        compile_ok, compile_stdout, compile_stderr = compile_csharp_dotnet()
    else:
        compile_ok, compile_stdout, compile_stderr = compile_csharp_mono()

# Em caso de erro de compilação: registra e sai
def persist_compile_error_and_exit(stdout_msg: str, stderr_msg: str):
    idle_cpu = psutil.cpu_percent(interval=1)
    idle_ram = psutil.virtual_memory().used / (1024 ** 2)
    linhas_codigo = sum(1 for _ in open(alg_path, 'r', encoding="utf-8", errors="ignore"))
    result = {
        "classe": classe,
        "problema": "knapsack" if classe == "np-completo" else None,
        "algoritmo": algoritmo_variant or None,
        "linguagem": linguagem,
        "tamanho": tamanho,
        "repeticao": int(repeticao),
        "tempo_s": 0.0,
        "cpu_before": idle_cpu,
        "ram_before_mb": round(idle_ram, 2),
        "cpu_avg_during": 0.0,
        "cpu_max_during": 0.0,
        "cpu_avg_during_norm": 0.0,
        "cpu_max_during_norm": 0.0,
        "ram_avg_during_mb": 0.0,
        "ram_max_during_mb": 0.0,
        "cpu_after": 0.0,
        "ram_after_mb": round(psutil.virtual_memory().used / (1024 ** 2), 2),
        "linhas_codigo": linhas_codigo,
        "timestamp": datetime.now().isoformat(),
        "especificacoes_sistema": specs,
        "stdout": stdout_msg,
        "stderr": stderr_msg,
        "exit_code": -1,
        "timeout_s": 0,
        "samples": 0,
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
# Monta comandos de execução
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

# Verifica runtime/ferramenta
first_exe = execucoes[ling][0]
if not (os.path.isfile(first_exe) or which(first_exe)):
    print(f"❌ Runtime/ferramenta não encontrada: {first_exe}")
    sys.exit(1)

# Baseline
idle_cpu = psutil.cpu_percent(interval=0.8)
idle_ram = psutil.virtual_memory().used / (1024 ** 2)

# Linhas de código
with open(alg_path, 'r', encoding="utf-8", errors="ignore") as code_file:
    linhas_codigo = sum(1 for _ in code_file)

metrics = []    # (cpu_total_pct, ram_max_mb)
SAMPLE_INTERVAL = 0.1
TIMEOUT_SEC     = int(os.environ.get("TIMEOUT_SEC", "180"))
timeout_hit = False
exit_code = None

def monitor_process(proc):
    """Amostragem de CPU/RAM de parent + children a cada SAMPLE_INTERVAL."""
    try:
        parent = psutil.Process(proc.pid)
        prime_cpu_counters(parent)
        while True:
            if proc.poll() is not None:
                # última leitura após término
                try:
                    procs = [parent] + parent.children(recursive=True)
                except psutil.NoSuchProcess:
                    procs = []
                cpu_total = 0.0
                ram_peak = 0.0
                for p in procs:
                    try:
                        cpu_total += p.cpu_percent(0.0)
                        ram_peak = max(ram_peak, p.memory_info().rss / (1024 ** 2))
                    except psutil.NoSuchProcess:
                        pass
                metrics.append((cpu_total, ram_peak))
                break

            try:
                procs = [parent] + parent.children(recursive=True)
            except psutil.NoSuchProcess:
                break

            cpu_total = 0.0
            ram_peak = 0.0
            for p in procs:
                try:
                    cpu_total += p.cpu_percent(0.0)   # relativo desde a última chamada
                    ram_peak = max(ram_peak, p.memory_info().rss / (1024 ** 2))
                except psutil.NoSuchProcess:
                    continue

            metrics.append((cpu_total, ram_peak))
            time.sleep(SAMPLE_INTERVAL)
    except Exception as e:
        print(f"[monitor] erro: {e}")

exec_cmd = execucoes[ling]

start = time.time()
proc = subprocess.Popen(exec_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

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

# Estatísticas
cpu_series = [m[0] for m in metrics]  # soma % por processo (pode passar de 100 em multi-core)
ram_series = [m[1] for m in metrics]

def mean(xs): return round(sum(xs)/len(xs), 2) if xs else 0.0

cpu_avg = mean(cpu_series)
cpu_max = round(max(cpu_series), 2) if cpu_series else 0.0
ram_avg = mean(ram_series)
ram_max = round(max(ram_series), 2) if ram_series else 0.0

# versões normalizadas por nº de núcleos (0..100%)
cpu_avg_norm = round(cpu_avg / N_CORES, 2)
cpu_max_norm = round(cpu_max / N_CORES, 2)

cpu_after = psutil.cpu_percent(interval=0.5)
ram_after = psutil.virtual_memory().used / (1024 ** 2)

result = {
    "classe": classe,
    "problema": "knapsack" if classe == "np-completo" else None,
    "algoritmo": algoritmo_variant or None,   # "exato"|"guloso"|None
    "linguagem": linguagem,
    "tamanho": tamanho,
    "repeticao": int(repeticao),

    "tempo_s": round(end - start, 6),

    "cpu_before": idle_cpu,
    "ram_before_mb": round(idle_ram, 2),

    "cpu_avg_during": cpu_avg,
    "cpu_max_during": cpu_max,
    "cpu_avg_during_norm": cpu_avg_norm,
    "cpu_max_during_norm": cpu_max_norm,
    "ram_avg_during_mb": ram_avg,
    "ram_max_during_mb": ram_max,

    "cpu_after": cpu_after,
    "ram_after_mb": round(ram_after, 2),

    "linhas_codigo": linhas_codigo,
    "timestamp": datetime.now().isoformat(),
    "especificacoes_sistema": specs,

    "stdout": stdout.decode(errors="replace"),
    "stderr": stderr.decode(errors="replace"),

    "exit_code": exit_code if exit_code is not None else -1,
    "timeout_s": TIMEOUT_SEC if timeout_hit else 0,
    "samples": len(metrics),
}

# ===================== Persistência =====================
output_file = os.path.join(OUT_DIR, "metricas.json")
try:
    if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
        with open(output_file, "r", encoding="utf-8") as f:
            all_results = json.load(f)
    else:
        all_results = []
except Exception:
    all_results = []

all_results.append(result)
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(all_results, f, indent=2, ensure_ascii=False)

print("✅ Finalizado e adicionado em: metricas.json")
