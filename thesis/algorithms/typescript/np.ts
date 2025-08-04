import * as fs from 'fs';
import * as path from 'path';

function parseNumbers(filePath: string): number[] {
  const content = fs.readFileSync(filePath, 'utf-8').trim();
  const cleaned = content.replace('[', '').replace(']', '');
  return cleaned
    .split(',')
    .map((s) => parseInt(s.trim()))
    .filter((n) => !isNaN(n));
}

function findFactors(n: number): [number, number] | null {
  for (let i = 2; i <= Math.floor(Math.sqrt(n)); i++) {
    if (n % i === 0) {
      return [i, n / i];
    }
  }
  return null;
}

function main() {
  const args = process.argv.slice(2);
  if (args.length < 1) {
    console.log('Uso: tsx np.ts <tamanho>');
    return;
  }

  const tamanho = args[0];
  const filePath = path.join('datasets', tamanho, 'factoring.json');

  if (!fs.existsSync(filePath)) {
    console.error(`Arquivo não encontrado: ${filePath}`);
    return;
  }

  try {
    const numbers = parseNumbers(filePath);
    let fatorados = 0;
    let primos = 0;

    for (const n of numbers) {
      if (findFactors(n)) {
        fatorados++;
      } else {
        primos++;
      }
    }

    console.log(`Fatorados: ${fatorados}`);
  } catch (err) {
    console.error(`Erro: ${(err as Error).message}`);
  }
}

main();
