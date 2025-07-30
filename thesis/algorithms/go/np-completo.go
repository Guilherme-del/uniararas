package main

import (
    "encoding/json"
    "fmt"
    "io/ioutil"
    "os"
)

type Item struct {
    Weight int `json:"weight"`
    Value  int `json:"value"`
}

type KnapsackInput struct {
    Capacity int    `json:"capacity"`
    Items    []Item `json:"items"`
}

func knapsack(items []Item, capacity int) int {
    dp := make([]int, capacity+1)
    for _, item := range items {
        for w := capacity; w >= item.Weight; w-- {
            if val := dp[w-item.Weight] + item.Value; val > dp[w] {
                dp[w] = val
            }
        }
    }
    return dp[capacity]
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
    fmt.Printf("Valor máximo para %d itens (%s): %d\n", len(input.Items), size, result)
}
