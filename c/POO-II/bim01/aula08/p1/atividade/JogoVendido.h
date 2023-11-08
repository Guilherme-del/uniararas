#ifndef JOGOVENDIDO_H
#define JOGOVENDIDO_H

#include "Jogo.h"

class JogoVendido : public Jogo {
public:
    JogoVendido(const std::string& nome, int faixaEtaria);
    void exibirDetalhes() override;
};

#endif
