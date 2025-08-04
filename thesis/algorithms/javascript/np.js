const fs = require('fs');
const path = require('path');

function hasFactor(n) {
  for (let i = 2; i * i <= n; i++) {
    if (n % i === 0) return true;
  }
  return false;
}

function main() {
  const tamanho = process.argv[2] || 'small';
  const datasetPath = path.join(__dirname, '..', '..', 'datasets', tamanho, 'factoring.json');

  try {
    const content = fs.readFileSync(datasetPath, 'utf8').trim();
    const numbers = JSON.parse(content);

    if (!Array.isArray(numbers) || numbers.length === 0) {
      console.log(`Nenhum número no dataset ${tamanho}.`);
      return;
    }

    let count = 0;
    for (const n of numbers) {
      if (hasFactor(n)) count++;
    }

    console.log(`Fatorados ${count} números do dataset ${tamanho}.`);
  } catch (err) {
    console.error('Erro ao ler ou processar o arquivo:', err.message);
  }
}

main();
