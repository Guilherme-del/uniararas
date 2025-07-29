import json
import sys

def evaluate_clause(clause, assignment):
    return any((lit > 0 and assignment.get(abs(lit), False)) or 
               (lit < 0 and not assignment.get(abs(lit), False)) 
               for lit in clause)

def is_satisfiable(cnf, num_vars):
    from itertools import product
    for bits in product([False, True], repeat=num_vars):
        assignment = {i + 1: bits[i] for i in range(num_vars)}
        if all(evaluate_clause(clause, assignment) for clause in cnf):
            return True
    return False

def main(size='small'):
    with open(f'../datasets/{size}/sat_{size}.json', 'r') as f:
        cnf = json.load(f)
    num_vars = 100  # Ajuste conforme necessário
    satisfiable = is_satisfiable(cnf, num_vars)
    print(f'{size.capitalize()} SAT instance is satisfiable? {satisfiable}')

if __name__ == '__main__':
    size = sys.argv[1] if len(sys.argv) > 1 else 'small'
    main(size)
