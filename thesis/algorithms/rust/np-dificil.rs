use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();
    let default_size = String::from("small");
    let size = args.get(1).unwrap_or(&default_size);
    let path = format!("datasets/{}/halting.json", size);

    let data = fs::read_to_string(&path).expect("Erro ao ler arquivo");

    // Remove colchetes e quebra em objetos individuais
    let content = data.trim();
    let content = content.trim_start_matches('[').trim_end_matches(']');
    let entries = content.split("},").collect::<Vec<&str>>();

    let mut halted = 0;
    let mut total = 0;

    for entry in entries {
        if entry.contains("\"program\"") {
            total += 1;
            if entry.contains("HALT") {
                halted += 1;
            }
        }
    }

    println!("{} de {} programas halting ({})", halted, total, size);
}
