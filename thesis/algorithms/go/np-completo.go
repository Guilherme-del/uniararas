package main

import (
    "encoding/json"
    "fmt"
    "io/ioutil"
    "os"
    "sort"
)

type Item struct {
    Weight int `json:"weight"`
    Value  int `json:"value"`
}

type KnapsackInput struct {
    Capacity int    `json:"capacity"`
    Items    []Item `json:"items"`
}

// Algoritmo guloso: ordena por valor/peso e adiciona enquanto possível
func knapsack(items []Item, capacity int) int {
    // Ordena por valor/peso decrescente
    sort.Slice(items, func(i, j int) bool {
        return float64(items[i].Value)/float64(items[i].Weight) >
            float64(items[j].Value)/float64(items[j].Weight)
    })

    totalValue := 0
    currentWeight := 0

    for _, item := range items {
        if currentWeight+item.Weight <= capacity {
            currentWeight += item.Weight
            totalValue += item.Value
        }
    }

    return totalValue
}

func main() {
    size := "small"
    if len(os.Args) > 1 {
        size = os.Args[1]
    }

    path := "datasets/" + size + "/knapsack.json"
    data, err := ioutil.ReadFile(path)
    if err != nil {
        fmt.Println("Erro ao ler arquivo:", err)
        return
    }

    var input KnapsackInput
    if err := json.Unmarshal(data, &input); err != nil {
        fmt.Println("Erro ao decodificar JSON:", err)
        return
    }

    result := knapsack(input.Items, input.Capacity)
    fmt.Printf("Valor aproximado (greedy) para %d itens (capacidade %d, %s): %d\n",
        len(input.Items), input.Capacity, size, result)
}
