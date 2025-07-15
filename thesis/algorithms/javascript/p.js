const fs = require('fs');

function mergeSort(arr) {
    if (arr.length <= 1) return arr;
    const mid = Math.floor(arr.length / 2);
    const left = mergeSort(arr.slice(0, mid));
    const right = mergeSort(arr.slice(mid));
    return merge(left, right);
}

function merge(left, right) {
    const result = [];
    let i = 0, j = 0;
    while (i < left.length && j < right.length) {
        result.push(left[i] <= right[j] ? left[i++] : right[j++]);
    }
    return result.concat(left.slice(i)).concat(right.slice(j));
}

function main() {
    const size = process.argv[2] || 'small';
    const path = `../data/${size}/merge_sort_${size}.json`;
    if (!fs.existsSync(path)) {
        console.error('Arquivo não encontrado.');
        return;
    }
    const arr = JSON.parse(fs.readFileSync(path));
    mergeSort(arr);
    console.log(`Ordenado ${arr.length} elementos (${size})`);
}

main();
