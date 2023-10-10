#include "JogoComprado.h"
#include <iostream>

JogoComprado::JogoComprado(const std::string& nome, int faixaEtaria) : Jogo(nome, faixaEtaria) {}

void JogoComprado::exibirDetalhes() {
    Jogo::exibirDetalhes();
    std::cout << "Tipo: Comprado" << std::endl;
}
