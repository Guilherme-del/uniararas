#include <iostream>
#include <float.h> // Obter o valor de infinito (DBL_MAX)
#include <vector> // receber os estados filhos
#include <cmath>  // funções max e min.

using namespace std;

double minimax(Estado * atual, bool eMax, double alfa, double beta, int profundidade){
    
    // Se o estado for folha, OU atingiu profundidade méxima
    if(atual->eFolha() || profundidade == 0){
        return atual->heuristica();
    }
    double h;
    // Verificar se o nó é de máximo ou mínimo.
    if(eMax){
        // Vez do MAX
        h = -DBL_MAX; // menos infinito.
        // Gerar os filhos de MAX
        vector <Estado *> filhos = atual->expandir();
        for(int i = 0; i < filhos.size(); i++){
            double hFilho = minimax(filhos[i], false, alfa, beta, profundidade - 1);
            h = max(h, hFilho);
            alfa = max(alfa, hFilho);
            // SEGREDO!!!
            if(alfa >= beta){
                return h;
            }
        }
    }else{
        // Vez do MIN
        h = DBL_MAX; // mais infinito.
        // Gerar os filhos de MIN
        vector <Estado *> filhos = atual->expandir();
        for(int i = 0; i < filhos.size(); i++){
            double hFilho = minimax(filhos[i], true, alfa, beta, profundidade - 1);
            h = min(h, hFilho);
            beta = min(beta, hFilho);
            if(alfa >= beta){
                return h;
            }
        }
    }
    // Se nenhuma poda ocorreu, propaga para o pai o h calculado!
    return h;
}

int main()
{
    

    return 0;
}