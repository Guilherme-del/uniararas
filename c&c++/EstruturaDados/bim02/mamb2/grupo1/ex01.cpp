/*
1) Escreva uma função para “apagar” uma pilha implementada por ponteiros.
*/
#include <iostream>
#include <cstdlib>

using namespace std;

struct no{
    int valor;
    no * proximo;
};

no * inicio = NULL;
no * fim = NULL;

void empilhar(int novoValor){
    no * novoNo = (no *) malloc(sizeof(no));
    novoNo->valor = novoValor;
    novoNo->proximo = NULL;
    // pilha vazia
    if(inicio == NULL){
        inicio = novoNo;
        fim = novoNo;
    }else{
        fim->proximo = novoNo;
        fim = novoNo;
    }
}

int topo(){
    return inicio->valor;
}

// -------------- FUNCAO APAGAR ------------------------
void apagar(){
    no * removido = inicio;
    if(inicio == fim){
        inicio = NULL;
        fim = NULL;
    }else{
        inicio = inicio-> proximo;
    }
    free(removido);
}

int main(){

    empilhar(8);                 // 8 -> TESTE
    empilhar(10);                // 8 10 -> TESTE
    empilhar(12);                // 8 10 12 -> TESTE
    cout << "seu topo é: " << topo() << endl;    // --> mostra 8
    apagar();                  // 10 12 14
    cout << "seu topo é: " << topo() << endl;    // --> mostra 10
    apagar();                  // 12 14                // 14
    cout << "seu topo é: " << topo() << endl;    // --> mostra 14.
    return 0;
}