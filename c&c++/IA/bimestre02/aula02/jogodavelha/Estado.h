#ifndef ESTADO
#define ESTADO

#include <vector>
using namespace std;

class Estado{
public:
    // Retorna TRUE se o jogo terminou
    virtual bool eFolha() = 0;
    // Retorna o valor que será propagado para o pai
    virtual double heuristica() = 0;
    // Gera os estados filhos
    virtual vector<Estado *> expandir() = 0; 
};
#endif