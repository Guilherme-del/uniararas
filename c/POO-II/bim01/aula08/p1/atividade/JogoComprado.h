#ifndef JOGOCOMPRADO_H
#define JOGOCOMPRADO_H

#include "Jogo.h"

class JogoComprado : public Jogo {
public:
    JogoComprado(const std::string& nome, int faixaEtaria);
    void exibirDetalhes() override;
};

#endif
