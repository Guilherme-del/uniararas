/*6. Faça um programa que leia 10 números do teclado armazene-os em um vetor e
imprima-os em tela.
*/
#include <iostream>
using namespace std;

int main()
{


    int QuantidadeLista = 10;
    int somatoria;
    
    double Vetor1[QuantidadeLista];
    
    for (int w = 0; w <= (QuantidadeLista-1); w++) {
        cout << "Digite um valor para adicionar ao vetor 1: ";
        cin >> Vetor1[w];
    }
    
    for (int y = 0; y <= QuantidadeLista-1; y++) {
        cout << "Valor: " << Vetor1[y] << endl;
    }
}