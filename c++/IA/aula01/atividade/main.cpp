#include <iostream>
#include <vector>
#include "EstadoMissionario.h"

using namespace std;

int main()
{
    vector <Estado *> ed;

    Estado * atual = new EstadoMissionario(3,3,0,0,'e'); // Não será instanciado ainda!!!
    EstadoMissionario * atualMissionario;
    
    // Inserir o estado inicial na estrutura de dados.
    ed.push_back(atual);

    while(!atual->eObjetivo()){
        // Retirar o elemento da estrutura de dados.
        ed.erase(ed.begin());
        // Gerar os filhos do estado atual
        vector <Estado *> filhos = atual->expandir();
        // Varrer o vector, adicionando na pilha.
        for(int i = 0; i < filhos.size(); i++){
            ed.push_back(filhos[i]);
        }
        // Obter o próximo candidato à expansão
        atual = ed[0];
    } 
    while(atual != NULL){
        atualMissionario = dynamic_cast<EstadoMissionario *>(atual);
        atualMissionario->imprime();
        atual = atualMissionario->pai;
    }
    return 0;
}