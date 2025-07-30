use std::env;
use std::fs;

fn evaluate_clause(clause: &Vec<i32>, assignment: &std::collections::HashMap<i32, bool>) -> bool {
    for &lit in clause {
        let var = lit.abs();
        if let Some(&val) = assignment.get(&var) {
            if (lit > 0 && val) || (lit < 0 && !val) {
                return true;
            }
        }
    }
    false
}

fn is_satisfiable(clauses: &Vec<Vec<i32>>, num_vars: usize) -> bool {
    let total = 1 << num_vars;
    for mask in 0..total {
        let mut assignment = std::collections::HashMap::new();
        for i in 0..num_vars {
            assignment.insert((i + 1) as i32, (mask >> i) & 1 == 1);
        }
        if clauses.iter().all(|clause| evaluate_clause(clause, &assignment)) {
            return true;
        }
    }
    false
}

fn parse_clauses(raw: &str) -> Vec<Vec<i32>> {
    raw.trim_matches(&['[', ']'][..])
        .split("],[")
        .map(|s| {
            s.split(',')
                .filter_map(|n| n.trim().parse::<i32>().ok())
                .collect::<Vec<i32>>()
        })
        .collect()
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let fallback = "small".to_string();
    let size = args.get(1).unwrap_or(&fallback);
    let path = format!("datasets/{}/sat.json", size); 
    let data = fs::read_to_string(&path).expect("Erro ao ler arquivo");
    let clauses = parse_clauses(&data);
    let satisfiable = is_satisfiable(&clauses, 20);
    println!("SAT ({}): {}", size, if satisfiable { "Satisfatível" } else { "Insatisfatível" });
}
