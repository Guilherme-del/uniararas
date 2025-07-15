package main

import (
    "encoding/json"
    "fmt"
    "io/ioutil"
    "math"
    "os"
)

func evaluateClause(clause []int, assignment map[int]bool) bool {
    for _, lit := range clause {
        val := assignment[int(math.Abs(float64(lit)))]
        if (lit > 0 && val) || (lit < 0 && !val) {
            return true
        }
    }
    return false
}

func isSatisfiable(clauses [][]int, numVars int) bool {
    total := 1 << numVars
    for mask := 0; mask < total; mask++ {
        assignment := make(map[int]bool)
        for i := 0; i < numVars; i++ {
            assignment[i+1] = (mask>>i)&1 == 1
        }
        allTrue := true
        for _, clause := range clauses {
            if !evaluateClause(clause, assignment) {
                allTrue = false
                break
            }
        }
        if allTrue {
            return true
        }
    }
    return false
}

func main() {
    size := "small"
    if len(os.Args) > 1 {
        size = os.Args[1]
    }

    path := "../data/" + size + "/sat_" + size + ".json"
    data, err := ioutil.ReadFile(path)
    if err != nil {
        fmt.Println("Erro ao ler arquivo:", err)
        return
    }

    var clauses [][]int
    if err := json.Unmarshal(data, &clauses); err != nil {
        fmt.Println("Erro ao decodificar JSON:", err)
        return
    }

    sat := isSatisfiable(clauses, 20)
    if sat {
        fmt.Printf("SAT (%s): Satisfatível\n", size)
    } else {
        fmt.Printf("SAT (%s): Insatisfatível\n", size)
    }
}
