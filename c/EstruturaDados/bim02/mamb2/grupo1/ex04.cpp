#include <iostream>
#include <cstdlib>
using namespace std;

 struct no{
    int valor;
    no * proximo;
};

no * inicio = NULL;
no * fim = NULL;

void enqueue(int novoValor){
    no * novoNo = (no *) malloc(sizeof(no));
    novoNo->valor = novoValor;
    novoNo->proximo = NULL;
    
    if(inicio == NULL){
        inicio = novoNo;
        fim = novoNo;
    }else{
        fim->proximo = novoNo;
        fim = novoNo;
    }
}

int first(){
    return inicio->valor;
}

void dequeue(){
    no * removido = inicio;
    if(inicio == fim){
        inicio = NULL;
        fim = NULL;
    }else{
        inicio = inicio->proximo;
    }
    free(removido);
}

int main()
{
    enqueue(8);  // TESTE ->  [8]
    enqueue(10); // TESTE ->  [8,10]
    cout << first() << endl;
    dequeue(); //TESTE -> [10]
    cout << first();

    return 0;
}