import json
import sys

def simulate_program(program):
    if program == "HALT":
        return True
    elif program == "WHILE TRUE":
        return False

def main(size='small'):
    with open(f'../data/{size}/halting_{size}.json', 'r') as f:
        programs = json.load(f)
    halted = sum(1 for p in programs if simulate_program(p["program"]))
    print(f'{halted}/{len(programs)} programs halted in {size} dataset')

if __name__ == '__main__':
    size = sys.argv[1] if len(sys.argv) > 1 else 'small'
    main(size)
