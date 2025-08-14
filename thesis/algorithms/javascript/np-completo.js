const fs = require('fs');

function knapsack(items, capacity) {
    // Ordena por valor/peso decrescente
    items.sort((a, b) => (b.value / b.weight) - (a.value / a.weight));

    let totalValue = 0;
    let currentWeight = 0;

    for (const item of items) {
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

    const data = JSON.parse(fs.readFileSync(path));
    const result = knapsack(data.items, data.capacity);
    console.log(`Valor aproximado (greedy) para ${data.items.length} itens (capacidade ${data.capacity}, ${size}): ${result}`);
}

main();
