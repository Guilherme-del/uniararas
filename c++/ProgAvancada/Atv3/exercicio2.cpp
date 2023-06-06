/*
*****************************************************************************
2. Um polígono convexo de n lados apresenta um número de diagonais (nd) diferente, que
pode ser calculado pela seguinte expressão:
Faça um programa que leia o número de lados do polígono (n) e calcule o número de
diagonais diferentes do polígono. Realize o cálculo somente se o valor lido em n for maior
que 2.
******************************************************************************
*/

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    double numeroDeDiagonais,numeroDeLados;

    cout << "Numero de lados do poligono ?";
    cin >> numeroDeLados;
    
    

    if (numeroDeLados > 2) {
    numeroDeDiagonais = (numeroDeLados*(numeroDeLados - 3)) / 2 ;
    cout << "Numero de diagonais diferentes do poligono é igual a: " << numeroDeDiagonais;
    }
    else {
      cout << "O numero de lados do poligono deve ser maior que 2 ";
      return 0;
    }
    return 0;
}
