import json
import sys

def knapsack(items, capacity):
    n = len(items)
    dp = [0] * (capacity + 1)
    for weight, value in items:
        for c in range(capacity, weight - 1, -1):
            dp[c] = max(dp[c], dp[c - weight] + value)
    return dp[capacity]

def main(size='small'):
    with open(f'../data/{size}/knapsack_{size}.json', 'r') as f:
        data = json.load(f)
    items = [(item["weight"], item["value"]) for item in data["items"]]
    capacity = data["capacity"]
    result = knapsack(items, capacity)
    print(f'Maximum value for {size} dataset: {result}')

if __name__ == '__main__':
    size = sys.argv[1] if len(sys.argv) > 1 else 'small'
    main(size)
