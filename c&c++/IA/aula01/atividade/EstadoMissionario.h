#ifndef ESTADO_MISSIONARIO_H
#define ESTADO_MISSIONARIO_H

// Incluir a interface que será implementada
#include "Estado.h"

class EstadoMissionario : public Estado{
  private:
    // atributos do problema.
    int mE;
    int mD;
    int cE;
    int cD;
    char barco;

    vector <Estado *> filhos;
  
  public:
      Estado * pai;
    // Dois construtores sobrecarregados
    EstadoMissionario(int mE, int cE, int mD, int cD, char barco);
    EstadoMissionario(Estado * pai, int mE, int cE, int mD, int cD, char barco);
    
    // Implementação por sobrescita dos métodos da interface.
    bool  eObjetivo();
    vector <Estado *> expandir();
    
    // Método para exibir na tela o estado.
    void imprime();
    
    // restrições do problema
    bool ePossivel();
    
    // Ações do problema
    EstadoMissionario * mover1Missionario();
    EstadoMissionario * mover2Missionario();
    EstadoMissionario * mover1Canibal();
    EstadoMissionario * mover2Canibal();
    EstadoMissionario * mover1Missionario1Canibal();
};

#endif