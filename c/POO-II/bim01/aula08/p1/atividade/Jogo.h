#ifndef JOGO_H
#define JOGO_H

#include <string>

class Jogo {
public:
    Jogo(const std::string& nome, int faixaEtaria);

    virtual void jogar(int horas);
    std::string getNome();
    int getFaixaEtaria();
    int getHorasJogadas();
    virtual void exibirDetalhes();

private:
    std::string nome;
    int faixaEtaria;
    int horasJogadas;
};

#endif
