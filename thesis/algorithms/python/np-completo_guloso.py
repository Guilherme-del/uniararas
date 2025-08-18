import json
import sys

def knapsack(items, capacity):
    # Ordenar por valor/peso decrescente
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_value = 0
    current_weight = 0

    for weight, value in items:
        if current_weight + weight <= capacity:
            current_weight += weight
            total_value += value

    return total_value

def main(size='small'):
    try:
        with open(f'datasets/{size}/knapsack.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Arquivo datasets/{size}/knapsack.json não encontrado.")
        return

    items = [(item["weight"], item["value"]) for item in data["items"]]
    capacity = data["capacity"]
    result = knapsack(items, capacity)
    print(f'Valor aproximado (greedy) para {len(items)} itens (capacidade {capacity}, {size}): {result}')

if __name__ == '__main__':
    size = sys.argv[1] if len(sys.argv) > 1 else 'small'
    main(size)
