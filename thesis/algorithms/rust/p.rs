use std::env;
use std::fs;

fn merge_sort(mut arr: Vec<i32>) -> Vec<i32> {
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

fn main() {
    let args: Vec<String> = env::args().collect();
    let size = args.get(1).unwrap_or(&"small".to_string());
    let path = format!("../data/{}/merge_sort_{}.json", size, size);
    let data = fs::read_to_string(&path).expect("Erro ao ler o arquivo");
    let arr: Vec<i32> = serde_json::from_str(&data).expect("Erro ao decodificar JSON");
    let sorted = merge_sort(arr.clone());
    println!("Ordenado {} elementos ({})", sorted.len(), size);
}
