import * as fs from 'fs';

interface Program {
    program: string;
}

function simulate(code: string): boolean {
    return code.trim().toUpperCase() === "HALT";
}

function main() {
    const size = process.argv[2] || 'small';
    const path = `../data/${size}/halting_${size}.json`;
    if (!fs.existsSync(path)) {
        console.error('Arquivo não encontrado.');
        return;
    }
    const programs: Program[] = JSON.parse(fs.readFileSync(path, 'utf-8'));
    const halted = programs.filter(p => simulate(p.program)).length;
    console.log(`${halted} de ${programs.length} programas halting (${size})`);
}

main();
