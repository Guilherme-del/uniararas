/*
6. Uma livraria está fazendo uma promoção para pagamento à vista em que o comprador
pode escolher entre dois critérios de desconto:
Faça um programa em que o usuário digita a quantidade de livros que deseja comprar e o
programa calcula qual seria o valor do pagamento em cada critério. O programa deve
afirmar quais dos critérios é mais vantajoso:
*/

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int livros;
    
    cout<<"Digite a quantidade de livros que vai comprar: ";
    cin>>livros;
    
    float A = 0.25 * livros + 7.5;
    float B = 0.50 * livros + 2.5;
    
    if (A < B) {
        cout<<"Critério A é mais vantajoso";
    }
    
    else if (B < A) {
        cout<<"Critério B é mais vantajoso";
    };

    return 0;
}
