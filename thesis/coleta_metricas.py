import os, psutil, time, subprocess, sys, json, platform, threading
from datetime import datetime
import distro

classe, linguagem, tamanho, repeticao = sys.argv[1:]

base_dir = os.path.dirname(os.path.abspath(__file__))

arquivo_por_classe = {
    "p": "p", "np": "np", "np-completo": "np-completo", "np-dificil": "np-dificil"
}
dataset_por_classe = {
    "p": "merge_sort.json", "np": "sat.json", "np-completo": "knapsack.json", "np-dificil": "halting.json"
}
extensao = {
    "c": "c", "c++": "cpp", "c#": "cs", "go": "go", "java": "java", "javascript": "js",
    "python": "py", "typescript": "ts", "kotlin": "kt", "rust": "rs"
}[linguagem.lower()]

nome_arquivo_base = arquivo_por_classe[classe]
nome_arquivo = f"{nome_arquivo_base}.{extensao}"

# Classe Java precisa ser nomeada corretamente
nome_classe_java = None
if linguagem.lower() == "java":
    nome_classe_java = ''.join(part.capitalize() for part in nome_arquivo_base.replace('-', ' ').split())
    nome_arquivo = f"{nome_classe_java}.java"

alg_path = os.path.join(base_dir, "algorithms", linguagem.lower(), nome_arquivo)
dataset_nome = dataset_por_classe[classe]
dataset_path = os.path.join(base_dir, "datasets", tamanho, dataset_nome)

if not os.path.exists(dataset_path):
    print(f"❌ Dataset não encontrado: {dataset_path}")
    sys.exit(1)

# Comandos de compilação e execução
compilacoes = {
    "c": ["gcc", alg_path, "-o", "bin/exe"],
    "c++": ["g++", alg_path, "-o", "bin/exe"],
    "c#": ["mcs", alg_path, "-out:bin/exe.exe"],
    "java": ["javac", alg_path],
    "kotlin": ["kotlinc", alg_path, "-include-runtime", "-d", "bin/main.jar"],
    "rust": ["rustc", alg_path, "-o", "bin/exe"]
}

execucoes = {
    "c": ["./bin/exe", tamanho],
    "c++": ["./bin/exe", tamanho],
    "c#": ["mono", "bin/exe.exe", tamanho],
    "go": ["go", "run", alg_path, tamanho],
    "java": ["java", "-cp", "bin", nome_classe_java, tamanho],
    "kotlin": ["java", "-jar", "bin/main.jar", tamanho],
    "rust": ["./bin/exe", tamanho],
    "javascript": ["node", alg_path, tamanho],
    "typescript": ["npx", "tsx", alg_path, tamanho],
    "python": ["python3", alg_path, tamanho]
}

specs = {
    "sistema_operacional": platform.system(),
    "distro": distro.name(pretty=True),
    "versao_os": distro.version(pretty=True),
    "kernel": platform.release(),
    "arquitetura": platform.machine(),
    "cpu_modelo": platform.processor(),
    "cpu_cores": psutil.cpu_count(logical=True),
    "memoria_total_mb": round(psutil.virtual_memory().total / (1024 ** 2), 2)
}

idle_cpu = psutil.cpu_percent(interval=1)
idle_ram = psutil.virtual_memory().used / (1024 ** 2)

with open(alg_path, 'r') as code_file:
    linhas_codigo = len(code_file.readlines())

# Compilação (se necessário)
ling = linguagem.lower()
if ling in compilacoes:
    comp_proc = subprocess.run(compilacoes[ling], capture_output=True, text=True)
    if comp_proc.returncode != 0:
        result = {
            "classe": classe,
            "linguagem": linguagem,
            "tamanho": tamanho,
            "repeticao": int(repeticao),
            "tempo_s": 0.0,
            "cpu_before": idle_cpu,
            "ram_before_mb": round(idle_ram, 2),
            "cpu_avg_during": 0.0,
            "cpu_max_during": 0.0,
            "ram_avg_during_mb": 0.0,
            "ram_max_during_mb": 0.0,
            "cpu_after": 0.0,
            "ram_after_mb": round(psutil.virtual_memory().used / (1024 ** 2), 2),
            "linhas_codigo": linhas_codigo,
            "timestamp": datetime.now().isoformat(),
            "especificacoes_sistema": specs,
            "stdout": comp_proc.stdout,
            "stderr": comp_proc.stderr
        }
        os.makedirs("resultados", exist_ok=True)
        output_file = os.path.join("resultados", "metricas.json")
        if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
            with open(output_file, "r") as f:
                all_results = json.load(f)
        else:
            all_results = []
        all_results.append(result)
        with open(output_file, "w") as f:
            json.dump(all_results, f, indent=2)
        print("❌ Erro na compilação. Resultado salvo.")
        sys.exit(1)

# Execução com monitoramento
metrics = []

def monitor_real_process(proc):
    try:
        parent = psutil.Process(proc.pid)
        while proc.poll() is None:
            children = parent.children(recursive=True)
            targets = [parent] + children
            cpu_total = 0.0
            ram_max = 0.0
            for p in targets:
                try:
                    cpu = p.cpu_percent(interval=0.1)
                    ram = p.memory_info().rss / (1024 ** 2)
                    cpu_total += cpu
                    ram_max = max(ram_max, ram)
                except psutil.NoSuchProcess:
                    continue
            metrics.append((cpu_total, ram_max))
    except Exception as e:
        print(f"Erro no monitoramento: {e}")

exec_cmd = execucoes[ling]
start = time.time()
proc = subprocess.Popen(exec_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
monitor_thread = threading.Thread(target=monitor_real_process, args=(proc,))
monitor_thread.start()
stdout, stderr = proc.communicate()
monitor_thread.join()
end = time.time()

cpu_metrics = [m[0] for m in metrics]
ram_metrics = [m[1] for m in metrics]

cpu_after = psutil.cpu_percent(interval=0.5)
ram_after = psutil.virtual_memory().used / (1024 ** 2)

cpu_avg = round(sum(cpu_metrics)/len(cpu_metrics), 2) if cpu_metrics else 0.0
cpu_max = round(max(cpu_metrics), 2) if cpu_metrics else 0.0

ram_avg = round(sum(ram_metrics)/len(ram_metrics), 2) if ram_metrics else 0.0
ram_max = round(max(ram_metrics), 2) if ram_metrics else 0.0

result = {
    "classe": classe,
    "linguagem": linguagem,
    "tamanho": tamanho,
    "repeticao": int(repeticao),
    "tempo_s": round(end - start, 6),
    "cpu_before": idle_cpu,
    "ram_before_mb": round(idle_ram, 2),
    "cpu_avg_during": cpu_avg,
    "cpu_max_during": cpu_max,
    "ram_avg_during_mb": ram_avg,
    "ram_max_during_mb": ram_max,
    "cpu_after": cpu_after,
    "ram_after_mb": round(ram_after, 2),
    "linhas_codigo": linhas_codigo,
    "timestamp": datetime.now().isoformat(),
    "especificacoes_sistema": specs,
    "stdout": stdout.decode(errors="replace"),
    "stderr": stderr.decode(errors="replace")
}

os.makedirs("resultados", exist_ok=True)
output_file = os.path.join("resultados", "metricas.json")

if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
    with open(output_file, "r") as f:
        all_results = json.load(f)
else:
    all_results = []

all_results.append(result)

with open(output_file, "w") as f:
    json.dump(all_results, f, indent=2)

print("✅ Finalizado e adicionado em: metricas.json")
