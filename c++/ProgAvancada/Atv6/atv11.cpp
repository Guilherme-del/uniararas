/*11. Faça um programa que calcule a média de8  alunos da FHO – Uniararas e
armazene a média em um vetor para posterior recuperação.
*/
#include <iostream>
using namespace std;

int main(){

    int QuantidadeLista = 8;
    double Nota1,Nota2,Media;
    double Vetor1[QuantidadeLista];
    
    for (int x = 0; x <= (QuantidadeLista - 1); x++){
        cout << "Digite um valor para Nota1: ";
        cin >> Nota1;
        
        cout << "Digite um valor para a Nota2: ";
        cin >> Nota2;
        
        Media = (Nota1 + Nota2) / 2;
        
        Vetor1[x] = Media;
    }
}