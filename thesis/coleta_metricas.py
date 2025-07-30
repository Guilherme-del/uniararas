import os, psutil, time, subprocess, sys, json, platform
from datetime import datetime

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

alg_path = os.path.join(base_dir, "algorithms", linguagem.lower(), f"{arquivo_por_classe[classe]}.{extensao}")

# ⏺ Nome do dataset com base no padrão
dataset_nome = dataset_por_classe[classe]
dataset_path = os.path.join(base_dir, "datasets", tamanho, dataset_nome)

if not os.path.exists(dataset_path):
    print(f"❌ Dataset não encontrado: {dataset_path}")
    sys.exit(1)

cmd = ""

# Linguagens que usam apenas o argumento "tamanho"
usa_apenas_tamanho = {"c", "c++", "c#", "java", "kotlin", "rust"}

# 🛠 Compilação e comandos por linguagem
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
    class_name = os.path.basename(alg_path).replace(".java", "")
    cmd = f"java -cp {base_dir}/bin {class_name} {tamanho}"

elif linguagem == "kotlin":
    class_name = os.path.basename(alg_path).replace(".kt", "")
    os.system(f"kotlinc {alg_path} -include-runtime -d bin/{class_name}.jar")
    cmd = f"java -jar bin/{class_name}.jar {tamanho}"

elif linguagem == "rust":
    out_bin = os.path.join(base_dir, "bin", f"{classe}_rust_{tamanho}")
    os.system(f"rustc {alg_path} -o {out_bin}")
    cmd = f"{out_bin} {tamanho}"

# Linguagens que usam o caminho completo do JSON
elif linguagem == "go":
    cmd = f"go run {alg_path} {dataset_path}"

elif linguagem == "javascript":
    cmd = f"node {alg_path} {dataset_path}"

elif linguagem == "python":
    cmd = f"python3 {alg_path} {dataset_path}"

elif linguagem == "typescript":
    cmd = f"npx tsx {alg_path} {dataset_path}"

else:
    print(f"❌ Linguagem '{linguagem}' ainda não suportada.")
    sys.exit(1)

# 📦 Especificações da máquina
specs = {
    "sistema_operacional": platform.system(),
    "distro": distro.name(pretty=True),
    "versao_os": platform.version(),
    "kernel": platform.release(),
    "arquitetura": platform.machine(),
    "cpu_modelo": platform.processor(),
    "cpu_cores": psutil.cpu_count(logical=True),
    "memoria_total_gb": round(psutil.virtual_memory().total / (1024 ** 3), 2)
}

# 🔹 Coleta de idle
idle_cpu = psutil.cpu_percent(interval=1)
idle_ram = psutil.virtual_memory().percent

# ▶️ Executa o algoritmo
start = time.time()
proc = subprocess.Popen(cmd, shell=True)
pid = proc.pid

cpu_list, mem_list = [], []

try:
    while proc.poll() is None:
        p = psutil.Process(pid)
        cpu_list.append(p.cpu_percent(interval=0.1))
        mem_list.append(p.memory_info().rss / (1024 * 1024))  # MB
except Exception as e:
    print("Erro:", e)

end = time.time()

# 📊 Resultado final
result = {
    "classe": classe,
    "linguagem": linguagem,
    "tamanho": tamanho,
    "repeticao": int(repeticao),
    "tempo_s": round(end - start, 4),
    "cpu_idle": idle_cpu,
    "ram_idle": idle_ram,
    "cpu_avg": round(sum(cpu_list) / len(cpu_list), 2) if cpu_list else 0,
    "ram_avg": round(sum(mem_list) / len(mem_list), 2) if mem_list else 0,
    "ram_max": round(max(mem_list), 2) if mem_list else 0,
    "timestamp": datetime.now().isoformat(),
    "especificacoes_sistema": specs
}

os.makedirs("resultados", exist_ok=True)
fname = f"{classe}_{linguagem}_{tamanho}_r{repeticao}.json"
with open(os.path.join("resultados", fname), "w") as f:
    json.dump(result, f, indent=2)

print("✅ Finalizado:", fname)
