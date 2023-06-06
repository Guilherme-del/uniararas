#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <cstdlib>

using namespace std;

typedef struct registro celula;
struct registro
{
    int x;
    celula *prox;
};

void insere(int n, celula *p);
void contaNos(celula *p);

int main()
{
    int n1;
    celula atual;
    int tecla = 10;
    celula *pointer;
    atual.prox = NULL; // <------------------- faltou
    pointer = &atual;
  
    while(tecla != 0)
    {
        cout << "====== MENU ======" << endl;
        cout << "1 - para inserir um número" << endl;
        cout << "2 - para ver a quantidade de elementos" << endl;
        cin >> tecla;
        getchar();
        cout << endl;

        if(tecla == 1)
        {
            cout << "Digite um numero" << endl;
            cin >> n1;
            getchar();
            insere(n1, &atual);
        }
        else if(tecla == 2)
        {
            contaNos(&atual);
        }
    }
}

void insere(int n, celula *p)
{
    celula *nova;
    nova = (celula *) malloc(sizeof(celula));
    nova->x = n;
    nova->prox = p->prox;
    p->prox = nova;
}

void contaNos(celula *p)
{
    int cont = 0;
    celula *aux;

    //cout << "Valor inicial de count:" << cont;

    if(p != NULL)
    {
        aux = p;
        while(aux != NULL)
        {
            cont++;
	    	aux = aux->prox;
        }
    }
    cout << " numeroDeNós: " <<  cont << endl;
}