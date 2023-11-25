#ifndef ESTADO_VELHA
#define ESTADO_VELHA

#include <iostream>
#include "Estado.h"
#include <cstdlib>
#include <vector>

using namespace std;

class EstadoJogoDaVelha : public Estado{
private:
    int tabuleiro[3][3];
    void copia(int origem[][3], int destino[][3]);
    bool eMax;
    bool ePermitido(int linha, int coluna);
public:
    EstadoJogoDaVelha(int tabuleiro[][3], bool eMax);
    EstadoJogoDaVelha * jogadaHumano();
    bool eFolha();
    double heuristica();
    vector<Estado *> expandir();
    void imprimir();
};
#endif