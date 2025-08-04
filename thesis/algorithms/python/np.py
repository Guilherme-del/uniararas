import sys

def parse_numbers(path):
    with open(path, "r") as f:
        content = f.read().strip()
    content = content.replace('[', '').replace(']', '')
    return [int(x.strip()) for x in content.split(',') if x.strip()]

def find_factors(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return (i, n // i)
    return None

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 np.py <tamanho>")
        return

    tamanho = sys.argv[1]
    path = f"datasets/{tamanho}/factoring.json"

    try:
        numbers = parse_numbers(path)

        total = len(numbers)
        fatorados = 0
        primos = 0

        for n in numbers:
            result = find_factors(n)
            if result:
                fatorados += 1
            else:
                primos += 1

        print(f"Fatorados: {fatorados}")


    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
