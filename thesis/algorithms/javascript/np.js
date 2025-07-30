const fs = require('fs');

function evaluateClause(clause, assignment) {
    return clause.some(lit => {
        const val = assignment[Math.abs(lit)];
        return (lit > 0 && val) || (lit < 0 && !val);
    });
}

function isSatisfiable(clauses, numVars) {
    const total = 1 << numVars;
    for (let mask = 0; mask < total; mask++) {
        const assignment = {};
        for (let i = 1; i <= numVars; i++) {
            assignment[i] = (mask >> (i - 1)) & 1;
        }
        if (clauses.every(clause => evaluateClause(clause, assignment))) return true;
    }
    return false;
}

function main() {
    const size = process.argv[2] || 'small';
    const path = `datasets/${size}/sat.json`;
    if (!fs.existsSync(path)) {
        console.error('Arquivo não encontrado.');
        return;
    }
    const clauses = JSON.parse(fs.readFileSync(path));
    const satisfiable = isSatisfiable(clauses, 20);
    console.log(`SAT (${size}): ${satisfiable ? "Satisfatível" : "Insatisfatível"}`);
}

main();
