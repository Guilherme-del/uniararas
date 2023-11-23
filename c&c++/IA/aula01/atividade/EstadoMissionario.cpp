#include "EstadoMissionario.h"
#include <cstdlib>
#include <iostream>

using namespace std;

// Dois construtores sobrecarregados
EstadoMissionario::EstadoMissionario(int mE, int cE, int mD, int cD, char barco){
    this->pai = NULL;
    this->mE  = mE;
    this->cE  = cE;
    this->mD  = mD;
    this->cD  = cD;
    this->barco = barco;
}

EstadoMissionario::EstadoMissionario(Estado * pai, int mE, int cE, int mD, int cD, char barco){
    this->pai = pai;
    this->mE  = mE;
    this->cE  = cE;
    this->mD  = mD;
    this->cD  = cD;
    this->barco = barco;
}

bool EstadoMissionario::ePossivel(){
    
    return (this->mE >= this->cE || this->mE == 0 ) && (this->mD >= this->cD || this->mD == 0) && 
           (this->mE + this->mD == 3 && this->cE + this->cD == 3);
}
    
// Implementação por sobrescita dos métodos da interface.
bool  EstadoMissionario::eObjetivo(){
    return (this->mE == 0 && this->cE == 0 && this->mD == 3 && this->cD == 3 && this->barco == 'd');    
}

// Ações do problema
EstadoMissionario * EstadoMissionario::mover1Missionario(){
    EstadoMissionario * filho;
    if(this->barco == 'e'){
        filho = new EstadoMissionario(this, this->mE-1, this->cE, this->mD + 1, this->cD, 'd');
          
    }
    else{
        filho = new EstadoMissionario(this, this->mE+1, this->cE, this->mD - 1, this->cD, 'e'); 
    }
    if(filho->ePossivel())
        return filho;
    
    return NULL;
}

EstadoMissionario * EstadoMissionario::mover2Missionario(){
    EstadoMissionario * filho;
    if(this->barco == 'e'){
        filho = new EstadoMissionario(this, this->mE-2, this->cE, this->mD + 2, this->cD, 'd');
    }
    else{
        filho = new EstadoMissionario(this, this->mE+2, this->cE, this->mD - 2, this->cD, 'e'); 
    }
    if(filho->ePossivel())
        return filho;
    
    return NULL;
}

EstadoMissionario * EstadoMissionario::mover1Canibal(){
    EstadoMissionario * filho;
    if(this->barco == 'e'){
        filho = new EstadoMissionario(this, this->mE, this->cE-1, this->mD, this->cD+1, 'd');
          
    }
    else{
        filho = new EstadoMissionario(this, this->mE, this->cE+1, this->mD, this->cD-1, 'e'); 
    }
    if(filho->ePossivel())
        return filho;
    
    return NULL;
}

EstadoMissionario * EstadoMissionario::mover2Canibal(){
    EstadoMissionario * filho;
    if(this->barco == 'e'){
        filho = new EstadoMissionario(this, this->mE, this->cE-2, this->mD, this->cD+2, 'd');
    }
    else{
        filho = new EstadoMissionario(this, this->mE, this->cE+2, this->mD, this->cD-2, 'e'); 
    }
    if(filho->ePossivel())
        return filho;
    
    return NULL;
}

EstadoMissionario * EstadoMissionario::mover1Missionario1Canibal(){
    EstadoMissionario * filho;
    if(this->barco == 'e'){
        filho = new EstadoMissionario(this, this->mE-1, this->cE-1, this->mD+1, this->cD+1, 'd');
    }
    else{
        filho = new EstadoMissionario(this, this->mE+1, this->cE+1, this->mD-1, this->cD-1, 'e'); 
    }
    if(filho->ePossivel())
        return filho;
    
    return NULL;
}


vector <Estado *> EstadoMissionario::expandir(){
    EstadoMissionario * filho1 = this->mover1Missionario();
    if(filho1 != NULL){
        this->filhos.push_back(filho1);
    }
    EstadoMissionario * filho2 = this->mover2Missionario();
    if(filho2 != NULL){
        this->filhos.push_back(filho2);
    }
    EstadoMissionario * filho3 = this->mover1Missionario1Canibal();
    if(filho3 != NULL){
        this->filhos.push_back(filho3);
    }
    EstadoMissionario * filho4 = this->mover1Canibal();
    if(filho4 != NULL){
        this->filhos.push_back(filho4);
    }
    EstadoMissionario * filho5 = this->mover2Canibal();
    if(filho5 != NULL){
        this->filhos.push_back(filho5);
    }
    return this->filhos;
    
}

void EstadoMissionario::imprime(){
    cout << this->mE << "M |   | " << this->mD << "M\n";
    if(this->barco == 'e'){
        cout << "   |*  |\n";
    }else{
        cout << "   |  *|\n";
    }
    cout << this->cE << "C |   | " << this->cD << "C\n\n";
}