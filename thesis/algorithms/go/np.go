package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
	"path/filepath"
)

func hasFactor(n int) bool {
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return true
		}
	}
	return false
}

func main() {
	tamanho := "small"
	if len(os.Args) > 1 {
		tamanho = os.Args[1]
	}

	path := filepath.Join("datasets", tamanho, "factoring.json")

	data, err := ioutil.ReadFile(path)
	if err != nil {
		fmt.Printf("Erro ao ler o arquivo: %v\n", err)
		return
	}

	var numeros []int
	if err := json.Unmarshal(data, &numeros); err != nil {
		fmt.Printf("Erro ao fazer parse do JSON: %v\n", err)
		return
	}

	count := 0
	for _, n := range numeros {
		if hasFactor(n) {
			count++
		}
	}

	fmt.Printf("Fatorados %d números do dataset %s.\n", count, tamanho)
}
