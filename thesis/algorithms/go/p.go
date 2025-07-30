package main

import (
    "encoding/json"
    "fmt"
    "io/ioutil"
    "os"
    "strconv"
)

func mergeSort(arr []int) []int {
    if len(arr) <= 1 {
        return arr
    }
    mid := len(arr) / 2
    left := mergeSort(arr[:mid])
    right := mergeSort(arr[mid:])
    return merge(left, right)
}

func merge(left, right []int) []int {
    result := []int{}
    i, j := 0, 0
    for i < len(left) && j < len(right) {
        if left[i] <= right[j] {
            result = append(result, left[i])
            i++
        } else {
            result = append(result, right[j])
            j++
        }
    }
    result = append(result, left[i:]...)
    result = append(result, right[j:]...)
    return result
}

func main() {
    size := "small"
    if len(os.Args) > 1 {
        size = os.Args[1]
    }
    path := "datasets/" + size + "/merge_sort.json"
    data, err := ioutil.ReadFile(path)
    if err != nil {
        fmt.Println("Erro ao ler arquivo:", err)
        return
    }

    var arr []int
    if err := json.Unmarshal(data, &arr); err != nil {
        fmt.Println("Erro ao decodificar JSON:", err)
        return
    }

    mergeSort(arr)
    fmt.Printf("Ordenado %d elementos (%s)\n", len(arr), size)
}
