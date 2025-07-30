use std::env;
use std::fs;

fn merge_sort(arr: Vec<i32>) -> Vec<i32> {
    if arr.len() <= 1 {
        return arr;
    }
    let mid = arr.len() / 2;
    let left = merge_sort(arr[..mid].to_vec());
    let right = merge_sort(arr[mid..].to_vec());
    merge(left, right)
}

fn merge(left: Vec<i32>, right: Vec<i32>) -> Vec<i32> {
    let mut merged = Vec::with_capacity(left.len() + right.len());
    let (mut i, mut j) = (0, 0);
    while i < left.len() && j < right.len() {
        if left[i] <= right[j] {
            merged.push(left[i]);
            i += 1;
        } else {
            merged.push(right[j]);
            j += 1;
        }
    }
    merged.extend_from_slice(&left[i..]);
    merged.extend_from_slice(&right[j..]);
    merged
}

fn parse_json_array(raw: &str) -> Vec<i32> {
    raw.trim_matches(|c| c == '[' || c == ']')
        .split(',')
        .filter_map(|s| s.trim().parse::<i32>().ok())
        .collect()
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let fallback = "small".to_string();
    let size = args.get(1).unwrap_or(&fallback);

    let path = format!("datasets/{}/merge_sort.json", size);
    let data = fs::read_to_string(&path).expect("Erro ao ler o arquivo");

    let arr: Vec<i32> = parse_json_array(&data);
    let sorted = merge_sort(arr);
    println!("Ordenado {} elementos ({})", sorted.len(), size);
}
