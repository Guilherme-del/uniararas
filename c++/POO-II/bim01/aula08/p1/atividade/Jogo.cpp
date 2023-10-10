#include "Jogo.h"
#include <iostream>

Jogo::Jogo(const std::string& nome, int faixaEtaria) : nome(nome), faixaEtaria(faixaEtaria), horasJogadas(0) {}

void Jogo::jogar(int horas) {
    horasJogadas += horas;
}

std::string Jogo::getNome() {
    return nome;
}

int Jogo::getFaixaEtaria() {
    return faixaEtaria;
}

int Jogo::getHorasJogadas() {
    return horasJogadas;
}

void Jogo::exibirDetalhes() {
    std::cout << "Nome: " << nome << ", Faixa Etária: " << faixaEtaria << ", Horas Jogadas: " << horasJogadas << "h" << std::endl;
}
