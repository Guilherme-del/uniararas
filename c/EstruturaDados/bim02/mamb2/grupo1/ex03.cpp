/*
3) Implemente uma nova função de inserção em lista sequencial de forma que ela insira N
cópias de um certo dado a partir de uma posição Pos.
*/

#include <iostream>
#include <cstdlib>

using namespace std;

struct no {
    int valor;
    no * proximo;
}

no * inicio = NULL;


void pushModificado (int valor, int pos, int quantidade) {
    no * novoNo = (no*)malloc(sizeof(No));
    
    novoNo -> valor = valor;
    int quantidadeElemento = 1;
    
    // Elemento Vazio
    if (inicio == NULL) {
        novoNo -> proximo == NULL; 
    }
    
    else {
    novoNo -> proximo = inicio;
        
        for (int i = 0; i = NULL; i++) {
            
            i = novoNo -> proximo;
            quantidadeElemento = quantidadeElemento + 1;
    
        }
        if (pos < quantidadeElemento) {
            No * aux = inicio;
            
            for (int i = 0; i < pos - 1; i++) {
                aux = aux -> proximo
            }
            if (aux -> proximo == NULL) {
                aux -> proximo = novoNo;
                novoNo -> proximo = NULL;
            }
             else {
                 novoNo -> proximo = aux -> proximo;
                 aux -> proximo = novoNo;
             }
        }
    }
}
