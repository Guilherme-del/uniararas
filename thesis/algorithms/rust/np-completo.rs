use std::env;
use std::fs;
use serde::Deserialize;

#[derive(Deserialize)]
struct Item {
    weight: usize,
    value: usize,
}

#[derive(Deserialize)]
struct KnapsackInput {
    capacity: usize,
    items: Vec<Item>,
}

fn knapsack(items: &[Item], capacity: usize) -> usize {
    let mut dp = vec![0; capacity + 1];
    for item in items {
        for w in (item.weight..=capacity).rev() {
            dp[w] = dp[w].max(dp[w - item.weight] + item.value);
        }
    }
    dp[capacity]
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let size = args.get(1).unwrap_or(&"small".to_string());
    let path = format!("../data/{}/knapsack_{}.json", size, size);
    let data = fs::read_to_string(&path).expect("Erro ao ler arquivo");
    let input: KnapsackInput = serde_json::from_str(&data).expect("Erro ao decodificar JSON");
    let result = knapsack(&input.items, input.capacity);
    println!("Valor máximo para {} itens ({}): {}", input.items.len(), size, result);
}
