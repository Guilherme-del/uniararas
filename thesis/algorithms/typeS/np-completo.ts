import * as fs from 'fs';

interface Item {
    weight: number;
    value: number;
}

interface KnapsackData {
    capacity: number;
    items: Item[];
}

function knapsack(items: Item[], capacity: number): number {
    const dp = Array(capacity + 1).fill(0);
    for (const item of items) {
        for (let w = capacity; w >= item.weight; w--) {
            dp[w] = Math.max(dp[w], dp[w - item.weight] + item.value);
        }
    }
    return dp[capacity];
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
    console.log(`Valor máximo para ${data.items.length} itens (${size}): ${result}`);
}

main();
