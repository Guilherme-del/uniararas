use std::env;
use std::fs;
use std::path::Path;

fn parse_numbers(path: &str) -> Result<Vec<u64>, Box<dyn std::error::Error>> {
    let content = fs::read_to_string(path)?;
    let trimmed = content.trim().trim_start_matches('[').trim_end_matches(']');
    let numbers = trimmed
        .split(',')
        .filter_map(|s| s.trim().parse::<u64>().ok())
        .collect();
    Ok(numbers)
}

fn find_factors(n: u64) -> Option<(u64, u64)> {
    for i in 2..=((n as f64).sqrt() as u64) {
        if n % i == 0 {
            return Some((i, n / i));
        }
    }
    None
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        println!("Uso: np <tamanho>");
        return;
    }

    let tamanho = &args[1];
    let path = format!("datasets/{}/factoring.json", tamanho);

    if !Path::new(&path).exists() {
        eprintln!("Arquivo não encontrado: {}", path);
        return;
    }

    match parse_numbers(&path) {
        Ok(numbers) => {
            let mut fatorados = 0;
            let mut primos = 0;

            for &n in &numbers {
                match find_factors(n) {
                    Some(_) => fatorados += 1,
                    None => primos += 1,
                }
            }

            println!("✅ Fatorados: {}", fatorados);
        }
        Err(e) => {
            eprintln!("Erro ao ler o arquivo: {}", e);
        }
    }
}
