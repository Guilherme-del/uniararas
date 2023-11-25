// main.cpp
#include <iostream>
#include "Estado.h"
#include "Solucao.h"


int main() {
    // Defina o estado inicial com as posições iniciais do macaco, da caixa e da banana
    Estado estadoInicial(1, 0, 1, 1, 0, 0, false);

    // Crie uma instância da classe Solucao com o estado inicial
    Solucao solucao(estadoInicial);

    // Encontre a solução
    solucao.encontrarSolucao();

    // Acesse a solução diretamente a partir do membro "solucao" e imprima-a
    const std::vector<Estado>& solucaoEncontrada = solucao.solucao;

    if (!solucaoEncontrada.empty()) {
        std::cout << "Solucao encontrada:" << std::endl;
        for (const Estado& estado : solucaoEncontrada) {
            estado.imprimir();
        }
    } else {
        std::cout << "Nao foi possivel encontrar uma solucao." << std::endl;
    }

    return 0;
}