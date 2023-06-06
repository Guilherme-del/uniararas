    /*4. Faça um programa que leia 10 números inteiros, armazene-os em um vetor,
solicite um valor de referência inteiro e:
a) imprima os números do vetor que são maiores que o valor referência
b) retorne quantos números armazenados no vetor são menores que o valor de
referência
c) retorne quantas vezes o valor de referência aparece no vetor
*/

#include <iostream>
using namespace std;

int main()
{


    int QuantidadeLista = 10;
    int VarReferencia, contagem;
    
    double Variavel[QuantidadeLista];
    
    
    for (int w = 0; w <= (QuantidadeLista-1); w++) {
        cout << "Digite um valor para adicionar a lista: ";
        cin >> Variavel[w];
    }
    
    cout << "A)" << endl;
    cout << "Digite um valor de referência: ";
    cin >> VarReferencia;
    for (int x = 0; x <= (QuantidadeLista - 1); x++){
        if (Variavel[x] > VarReferencia) {
            cout << "Valor maior que o valor de referência: " << Variavel[x] << endl;
        }
    }
    
    cout << "B)" << endl;
    for (int y = 0; y <= (QuantidadeLista - 1); y++){
        if (Variavel[y] < VarReferencia) {
            contagem = contagem + 1;
        }
    }
    cout << "A quantidade de valores menores que o ponto de referência é: " << contagem << endl;
    
    cout << "C)";
    for (int z = 0; z <= (QuantidadeLista - 1); z++){
        if (Variavel[z] == VarReferencia) {
            contagem = contagem + 1;
        }
    }
    cout << "A quantidade de valores iguais ao ponto de referência é: " << contagem << endl;
}