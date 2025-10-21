import os
import json
import random

BASE_PATH = "datasets"
SIZES = {
    "small": 1000,
    "medium": 10000,
    "large": 100000,
}

os.makedirs(BASE_PATH, exist_ok=True)

# ---------- Dataset Generators ---------- #

def generate_factoring_dataset(n):
    """Generate numbers to be factored."""
    return [{"number": random.randint(10**5, 10**9)} for _ in range(n)]

def generate_halting_dataset(n):
    """Generate random pseudo-program descriptions."""
    ops = ["ADD", "SUB", "MUL", "DIV", "JMP", "CMP", "NOP"]
    return [{"program": [random.choice(ops) for _ in range(random.randint(5, 20))]} for _ in range(n)]

def generate_knapsack_dataset(n):
    """Generate knapsack items and capacities."""
    dataset = []
    for _ in range(n):
        num_items = random.randint(5, 15)
        items = [
            {"weight": random.randint(1, 50), "value": random.randint(10, 500)}
            for _ in range(num_items)
        ]
        capacity = random.randint(30, 200)
        dataset.append({"items": items, "capacity": capacity})
    return dataset

def generate_merge_sort_dataset(n):
    """Generate arrays to be sorted."""
    return [{"array": [random.randint(0, 1000000) for _ in range(random.randint(10, 100))]} for _ in range(n)]

# ---------- Generation Runner ---------- #

def save_dataset(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def main():
    for size_name, count in SIZES.items():
        print(f"Generating {size_name} datasets ({count} entries each)...")
        size_dir = os.path.join(BASE_PATH, size_name)
        os.makedirs(size_dir, exist_ok=True)

        datasets = {
            "factoring.json": generate_factoring_dataset(count),
            "halting.json": generate_halting_dataset(count),
            "knapsack.json": generate_knapsack_dataset(count),
            "merge_sort.json": generate_merge_sort_dataset(count),
        }

        for filename, data in datasets.items():
            path = os.path.join(size_dir, filename)
            save_dataset(path, data)

        print(f"✅ {size_name} datasets generated in {size_dir}\n")

if __name__ == "__main__":
    main()
