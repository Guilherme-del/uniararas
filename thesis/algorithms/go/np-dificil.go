package main

import (
    "encoding/json"
    "fmt"
    "io/ioutil"
    "os"
    "strings"
)

type Program struct {
    Program string `json:"program"`
}

func simulate(code string) bool {
    return strings.ToUpper(strings.TrimSpace(code)) == "HALT"
}

func main() {
    size := "small"
    if len(os.Args) > 1 {
        size = os.Args[1]
    }
    path := "../datasets/" + size + "/halting_" + size + ".json"

    data, err := ioutil.ReadFile(path)
    if err != nil {
        fmt.Println("Erro ao ler arquivo:", err)
        return
    }

    var programs []Program
    if err := json.Unmarshal(data, &programs); err != nil {
        fmt.Println("Erro ao decodificar JSON:", err)
        return
    }

    halted := 0
    for _, p := range programs {
        if simulate(p.Program) {
            halted++
        }
    }

    fmt.Printf("%d de %d programas halting (%s)\n", halted, len(programs), size)
}
