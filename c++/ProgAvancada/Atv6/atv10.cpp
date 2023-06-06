/*10. Faça um programa que armazene 10 pontos de coordenadas x e y. Armazene
todos os valores da componente x em um vetor chamado “x” e todos os valores da
componente “y” em outro vetor chamado “y”.
*/
#include <iostream>
using namespace std;

int main()
{


    int QuantidadeLista = 16;
    int par;
    double VetorX[8], VetorY[8];
    
    for (int x = 0; x <= (QuantidadeLista - 1); x++){
        par = x % 2;
        
        if (par != 0) {
            cout << "Digite um valor para a coordenada X: ";
            cin >> VetorX[x];
        }
        
        if (par == 0) {
          cout << "Digite um valor para coordenada Y: ";
          cin >> VetorY[x + 1];
        }
    }
}