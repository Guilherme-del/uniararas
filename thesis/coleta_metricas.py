import os, psutil, time, subprocess, sys, json, platform, threading
from datetime import datetime
import distro

classe, linguagem, tamanho, repeticao = sys.argv[1:]

base_dir = os.path.dirname(os.path.abspath(__file__))

arquivo_por_classe = {"p": "p", "np": "np", "np-completo": "np-completo", "np-dificil": "np-dificil"}

dataset_por_classe = {"p": "merge_sort.json", "np": "sat.json", "np-completo": "knapsack.json", "np-dificil": "halting.json"}

extensao = {"c": "c", "c++": "cpp", "c#": "cs", "go": "go", "java": "java", "javascript": "js", "python": "py", "typescript": "ts", "kotlin": "kt", "rust": "rs"}[linguagem.lower()]

nome_arquivo_base = arquivo_por_classe[classe]
nome_arquivo = f"{nome_arquivo_base}.{extensao}"

# Nome da classe para Java, se aplicável
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

cmd_dict = {
    "c": f"gcc {alg_path} -o bin/exe && ./bin/exe {tamanho}",
    "c++": f"g++ {alg_path} -o bin/exe && ./bin/exe {tamanho}",
    "c#": f"mcs {alg_path} -out:bin/exe.exe && mono bin/exe.exe {tamanho}",
    "go": f"go run {alg_path} {tamanho}",
    "java": f"javac {alg_path} -d bin && java -cp bin {nome_classe_java} {tamanho}",
    "javascript": f"node {alg_path} {tamanho}",
    "kotlin": f"kotlinc {alg_path} -include-runtime -d bin/main.jar && java -jar bin/main.jar {tamanho}",
    "python": f"python3 {alg_path} {tamanho}",
    "typescript": f"npx tsx {alg_path} {tamanho}",
    "rust": f"rustc {alg_path} -o bin/exe && ./bin/exe {tamanho}"
}

if linguagem.lower() not in cmd_dict:
    print(f"❌ Linguagem '{linguagem}' ainda não suportada.")
    sys.exit(1)

cmd = cmd_dict[linguagem.lower()]

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

metrics = []

def monitor_process(pid):
    try:
        p = psutil.Process(pid)
        p.cpu_percent(interval=None)
        while p.is_running():
            cpu = p.cpu_percent(interval=0.01)
            ram = p.memory_info().rss / (1024 ** 2)
            metrics.append((cpu, ram))
    except psutil.NoSuchProcess:
        pass

start = time.time()
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
monitor_thread = threading.Thread(target=monitor_process, args=(proc.pid,))
monitor_thread.start()
stdout, stderr = proc.communicate()
monitor_thread.join()
end = time.time()

cpu_metrics = [m[0] for m in metrics]
ram_metrics = [m[1] for m in metrics]

cpu_after = psutil.cpu_percent(interval=0.5)
ram_after = psutil.virtual_memory().used / (1024 ** 2)

result = {
    "classe": classe,
    "linguagem": linguagem,
    "tamanho": tamanho,
    "repeticao": int(repeticao),
    "tempo_s": round(end - start, 6),
    "cpu_before": idle_cpu,
    "ram_before_mb": round(idle_ram, 2),
    "cpu_avg_during": round(sum(cpu_metrics)/len(cpu_metrics), 2),
    "cpu_max_during": round(max(cpu_metrics), 2),
    "cpu_min_during": round(min(cpu_metrics), 2),
    "ram_avg_during_mb": round(sum(ram_metrics)/len(ram_metrics), 2),
    "ram_max_during_mb": round(max(ram_metrics), 2),
    "ram_min_during_mb": round(min(ram_metrics), 2),
    "cpu_after": cpu_after,
    "ram_after_mb": round(ram_after, 2),
    "linhas_codigo": linhas_codigo,
    "timestamp": datetime.now().isoformat(),
    "especificacoes_sistema": specs,
    "stdout": stdout.decode(errors="replace"),
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
