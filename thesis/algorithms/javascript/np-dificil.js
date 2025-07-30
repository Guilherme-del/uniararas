const fs = require('fs');

function simulate(program) {
    return program.trim().toUpperCase() === "HALT";
}

function main() {
    const size = process.argv[2] || 'small';
    const path = `datasets/${size}/halting.json`;
    if (!fs.existsSync(path)) {
        console.error('Arquivo não encontrado.');
        return;
    }
    const programs = JSON.parse(fs.readFileSync(path));
    const halted = programs.filter(p => simulate(p.program)).length;
    console.log(`${halted} de ${programs.length} programas halting (${size})`);
}

main();
