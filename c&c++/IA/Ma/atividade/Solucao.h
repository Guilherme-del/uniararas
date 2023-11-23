// Solucao.h
#ifndef SOLUCAO_H
#define SOLUCAO_H

#include "Estado.h"
#include <vector>

class Solucao {
public:
    std::vector<Estado> solucao;
    Solucao(const Estado& estadoInicial);
    void imprimirSolucao() const;
    void encontrarSolucao();

private:
    Estado estadoInicial;

    bool buscarSolucao(const Estado& estadoAtual);

    void acaoAndarEsquerda(Estado& estado);
    void acaoAndarDireita(Estado& estado);
    void acaoSubirSobreCaixa(Estado& estado);
    void acaoDescerDaCaixa(Estado& estado);
    void acaoPuxarCaixa(Estado& estado);
    void acaoEmpurrarCaixa(Estado& estado);
};

#endif
