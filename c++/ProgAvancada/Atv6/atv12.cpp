/*12. Faça um programa que dado um vetor “a” de 4 posições lido a partir do teclado,
apresente como output os valores de suas posições elevados ao quadrado.
Ex.: Input: a = [1,2,3,5]
Output: a = [1,4,9,25]
*/
#include <iostream>
using namespace std;

int main()
{


    int QuantidadeLista = 4;
    double Vetor1[QuantidadeLista], Vetor2[QuantidadeLista];
    
    for (int x = 0; x <= (QuantidadeLista - 1); x++){
        cout << "Digite um valor para o vetor 1: ";
        cin >> Vetor1[x];
    }
    
    for (int y = 0; y <= (QuantidadeLista -1); y++){
        Vetor2[y] = Vetor1[y]*Vetor1[y];
    }
    
    for (int z = 0; z <= (QuantidadeLista - 1); z++) {
        cout << "Valor: " << Vetor2[z] << endl;
    }
}