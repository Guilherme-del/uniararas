import * as fs from 'fs';

interface Item {
    weight: number;
    value: number;
}

interface KnapsackData {
    capacity: number;
    items: Item[];
}

// Algoritmo guloso: ordena por valor/peso e preenche enquanto houver capacidade
function knapsack(items: Item[], capacity: number): number {
    const sorted = [...items].sort((a, b) => (b.value / b.weight) - (a.value / a.weight));

    let totalValue = 0;
    let currentWeight = 0;

    for (const item of sorted) {
        if (currentWeight + item.weight <= capacity) {
            currentWeight += item.weight;
            totalValue += item.value;
        }
    }

    return totalValue;
}

function main() {
    const size = process.argv[2] || 'small';
    const path = `datasets/${size}/knapsack.json`;

    if (!fs.existsSync(path)) {
        console.error('Arquivo não encontrado.');
        return;
    }

    const data: KnapsackData = JSON.parse(fs.readFileSync(path, 'utf-8'));
    const result = knapsack(data.items, data.capacity);
    console.log(`Valor aproximado (greedy) para ${data.items.length} itens (capacidade ${data.capacity}, ${size}): ${result}`);
}

main();
