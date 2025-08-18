use std::env;
use std::fs;

#[derive(Debug, Clone)] // <- necessário para permitir .to_vec()
struct Item {
    weight: usize,
    value: usize,
}

fn parse_knapsack_json(path: &str) -> (usize, Vec<Item>) {
    let content = fs::read_to_string(path).expect("Erro ao ler o arquivo");

    // Extrair capacidade
    let cap_prefix = "\"capacity\":";
    let cap_start = content.find(cap_prefix).expect("Capacidade não encontrada") + cap_prefix.len();
    let cap_end = content[cap_start..].find(',').unwrap_or(10) + cap_start;
    let capacity: usize = content[cap_start..cap_end].trim().parse().unwrap();

    // Extrair itens
    let mut items = Vec::new();
    let mut remaining = content.as_str();
    while let Some(weight_idx) = remaining.find("\"weight\"") {
        remaining = &remaining[weight_idx..];
        let w_start = remaining.find(':').unwrap() + 1;
        let w_end = remaining[w_start..].find(',').unwrap() + w_start;
        let weight: usize = remaining[w_start..w_end].trim().parse().unwrap();

        let val_idx = remaining.find("\"value\"").unwrap();
        let v_start = remaining[val_idx..].find(':').unwrap() + val_idx + 1;
        let v_end = remaining[v_start..].find(|c: char| c == '}' || c == ',').unwrap() + v_start;
        let value: usize = remaining[v_start..v_end].trim().parse().unwrap();

        items.push(Item { weight, value });
        remaining = &remaining[v_end..];
    }

    (capacity, items)
}

// Versão gulosa (greedy): ordena por valor/peso e preenche até o limite
fn knapsack(items: &[Item], capacity: usize) -> usize {
    let mut sorted = items.to_vec(); // <- exige Clone

    sorted.sort_by(|a, b| {
        let r1 = b.value as f64 / b.weight as f64;
        let r2 = a.value as f64 / a.weight as f64;
        r1.partial_cmp(&r2).unwrap()
    });

    let mut total_value = 0;
    let mut current_weight = 0;

    for item in sorted {
        if current_weight + item.weight <= capacity {
            current_weight += item.weight;
            total_value += item.value;
        }
    }

    total_value
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let size = args.get(1).map(|s| s.as_str()).unwrap_or("small");
    let path = format!("datasets/{}/knapsack.json", size);
    let (capacity, items) = parse_knapsack_json(&path);

    if items.is_empty() {
        println!("Erro: nenhum item encontrado.");
        return;
    }

    let result = knapsack(&items, capacity);
    println!(
        "Valor aproximado (greedy) para {} itens (capacidade {}, {}): {}",
        items.len(),
        capacity,
        size,
        result
    );
}
