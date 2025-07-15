use std::env;
use std::fs;

#[derive(serde::Deserialize)]
struct Program {
    program: String,
}

fn simulate(code: &str) -> bool {
    code.trim().to_uppercase() == "HALT"
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let size = args.get(1).unwrap_or(&"small".to_string());
    let path = format!("../data/{}/halting_{}.json", size, size);
    let data = fs::read_to_string(&path).expect("Erro ao ler arquivo");
    let programs: Vec<Program> = serde_json::from_str(&data).expect("Erro ao decodificar JSON");

    let halted = programs.iter().filter(|p| simulate(&p.program)).count();
    println!("{} de {} programas halting ({})", halted, programs.len(), size);
}
