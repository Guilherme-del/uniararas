import os, psutil, time, subprocess, sys, json, platform
from datetime import datetime
import distro

classe, linguagem, tamanho, repeticao = sys.argv[1:]

base_dir = os.path.dirname(os.path.abspath(__file__))

arquivo_por_classe = {
    "p": "p",
    "np": "np",
    "np-completo": "np-completo",
    "np-dificil": "np-dificil"
}

dataset_por_classe = {
    "p": "merge_sort.json",
    "np": "sat.json",
    "np-completo": "knapsack.json",
    "np-dificil": "halting.json"
}

extensao = {
    "c": "c",
    "c++": "cpp",
    "c#": "cs",
    "go": "go",
    "java": "java",
    "javascript": "js",
    "python": "py",
    "typescript": "ts",
    "kotlin": "kt",
    "rust": "rs"
}[linguagem.lower()]

nome_arquivo_base = arquivo_por_classe[classe]
nome_arquivo = f"{nome_arquivo_base}.{extensao}"

if linguagem.lower() == "java":
    nome_arquivo = ''.join(part.capitalize() for part in nome_arquivo_base.split('-')) + ".java"

alg_path = os.path.join(base_dir, "algorithms", linguagem.lower(), nome_arquivo)

dataset_nome = dataset_por_classe[classe]
dataset_path = os.path.join(base_dir, "datasets", tamanho, dataset_nome)

if not os.path.exists(dataset_path):
    print(f"❌ Dataset não encontrado: {dataset_path}")
    sys.exit(1)

cmd = ""

if linguagem == "c":
    bin_path = os.path.join(base_dir, "bin", f"{classe}_c_{tamanho}")
    os.system(f"gcc {alg_path} -o {bin_path}")
    cmd = f"{bin_path} {tamanho}"
elif linguagem == "c++":
    bin_path = os.path.join(base_dir, "bin", f"{classe}_cpp_{tamanho}")
    os.system(f"g++ {alg_path} -o {bin_path}")
    cmd = f"{bin_path} {tamanho}"
elif linguagem == "c#":
    exe_path = os.path.join(base_dir, "bin", f"{classe}_cs_{tamanho}.exe")
    os.system(f"mcs {alg_path} -out:{exe_path}")
    cmd = f"mono {exe_path} {tamanho}"
elif linguagem == "java":
    os.system(f"javac {alg_path} -d {base_dir}/bin")
    class_name = os.path.splitext(os.path.basename(alg_path))[0]
    cmd = f"java -cp {base_dir}/bin {class_name} {tamanho}"
elif linguagem == "kotlin":
    class_name = os.path.basename(alg_path).replace(".kt", "")
    os.system(f"kotlinc {alg_path} -include-runtime -d bin/{class_name}.jar")
    cmd = f"java -jar bin/{class_name}.jar {tamanho}"
elif linguagem == "rust":
    out_bin = os.path.join(base_dir, "bin", f"{classe}_rust_{tamanho}")
    os.system(f"rustc {alg_path} -o {out_bin}")
    cmd = f"{out_bin} {tamanho}"
elif linguagem == "go":
    cmd = f"go run {alg_path} {tamanho}"
elif linguagem == "javascript":
    cmd = f"node {alg_path} {tamanho}"
elif linguagem == "python":
    cmd = f"python3 {alg_path} {tamanho}"
elif linguagem == "typescript":
    cmd = f"npx tsx {alg_path} {tamanho}"
else:
    print(f"❌ Linguagem '{linguagem}' ainda não suportada.")
    sys.exit(1)

specs = {
    "sistema_operacional": platform.system(),
    "distro": distro.name(pretty=True),
    "versao_os": distro.version(pretty=True),
    "kernel": platform.release(),
    "arquitetura": platform.machine(),
    "cpu_modelo": platform.processor(),
    "cpu_cores": psutil.cpu_count(logical=True),
    "memoria_total_gb": round(psutil.virtual_memory().total / (1024 ** 3), 2)
}

idle_cpu = psutil.cpu_percent(interval=1)
idle_ram = psutil.virtual_memory().percent

start = time.time()
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
pid = proc.pid

cpu_list, mem_list = [], []

try:
    while proc.poll() is None:
        try:
            p = psutil.Process(pid)
            cpu_list.append(p.cpu_percent(interval=0.05))
            mem_list.append(p.memory_info().rss / (1024 * 1024))  # MB
        except Exception:
            break  # Processo já morreu

    # Fallback: tenta pegar uma última amostra após o processo terminar
    try:
        p = psutil.Process(pid)
        cpu_list.append(p.cpu_percent(interval=0.01))
        mem_list.append(p.memory_info().rss / (1024 * 1024))
    except Exception:
        pass
except Exception as e:
    print("Erro:", e)

stdout, stderr = proc.communicate()
stdout = stdout.decode(errors="replace")
stderr = stderr.decode(errors="replace")

end = time.time()

result = {
    "classe": classe,
    "linguagem": linguagem,
    "tamanho": tamanho,
    "repeticao": int(repeticao),
    "tempo_s": round(end - start, 4),
    "cpu_idle": idle_cpu,
    "ram_idle": idle_ram,
    "cpu_max": round(max(cpu_list), 2) if cpu_list else 0,
    "ram_max": round(max(mem_list), 2) if mem_list else 0,
    "timestamp": datetime.now().isoformat(),
    "especificacoes_sistema": specs,
    "stdout": stdout,
    "stderr": stderr
}

os.makedirs("resultados", exist_ok=True)
output_file = os.path.join("resultados", "metricas.json")

if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
    with open(output_file, "r") as f:
        try:
            all_results = json.load(f)
        except json.JSONDecodeError:
            all_results = []
else:
    all_results = []

all_results.append(result)

with open(output_file, "w") as f:
    json.dump(all_results, f, indent=2)

print("✅ Finalizado e adicionado em: metricas.json")
