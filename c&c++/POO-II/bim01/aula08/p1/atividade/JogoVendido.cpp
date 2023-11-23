#include "JogoVendido.h"
#include <iostream>

JogoVendido::JogoVendido(const std::string& nome, int faixaEtaria) : Jogo(nome, faixaEtaria) {}

void JogoVendido::exibirDetalhes() {
    Jogo::exibirDetalhes();
    std::cout << "Tipo: Vendido" << std::endl;
}