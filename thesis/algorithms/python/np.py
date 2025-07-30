import json
import sys
import os

def evaluate_clause(clause, assignment):
    for lit in clause:
        val = assignment.get(abs(lit), 0)
        if (lit > 0 and val) or (lit < 0 and not val):
            return True
    return False

def is_satisfiable(clauses, num_vars):
    total = 1 << num_vars
    for mask in range(total):
        assignment = {i: (mask >> (i - 1)) & 1 for i in range(1, num_vars + 1)}
        if all(evaluate_clause(clause, assignment) for clause in clauses):
            return True
    return False

def main():
    size = sys.argv[1] if len(sys.argv) > 1 else 'small'
    path = f'datasets/{size}/sat.json'
    if not os.path.exists(path):
        print("Arquivo não encontrado.")
        return

    with open(path, 'r') as f:
        clauses = json.load(f)

    satisfiable = is_satisfiable(clauses, 20)
    print(f"SAT ({size}): {'Satisfatível' if satisfiable else 'Insatisfatível'}")

if __name__ == '__main__':
    main()
