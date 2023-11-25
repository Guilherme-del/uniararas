#include <iostream>
#include <float.h> // Obter o valor de infinito (DBL_MAX)
#include <vector> // receber os estados filhos
#include <cmath>  // funções max e min.
#include "EstadoJogoDaVelha.h"
using namespace std;

EstadoJogoDaVelha * escolhaIA;
double maiorH = -DBL_MAX;
int maxProfundide = 9;

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
            // Tô na raiz?
            if(profundidade == maxProfundide){
                if(h > maiorH){
                    maiorH = h;
                    escolhaIA = dynamic_cast<EstadoJogoDaVelha *>(filhos[i]);
                }
            }
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
    int tabuleiro[][3] = {
        {0,0,0},
        {0,0,0},
        {0,0,0}
    };
    
    EstadoJogoDaVelha * atual = new EstadoJogoDaVelha(tabuleiro, true);
    // Enquanto o jogo não acabar ... 
    while(!atual->eFolha()){
        maiorH = -DBL_MAX;
        double h = minimax(atual, true, -DBL_MAX, DBL_MAX, maxProfundide);
        escolhaIA->imprimir();
        if(escolhaIA->eFolha()){
            if(h == 3){
                cout << "IA venceu!!!" << endl;
            }
            break;
        }
        atual = escolhaIA->jogadaHumano();
        h = atual->heuristica();
        if(atual->eFolha()){
            if(h == -3){
                cout << "Humano venceu!!!" << endl;
            }
            break;
        }
    }
    return 0;
}