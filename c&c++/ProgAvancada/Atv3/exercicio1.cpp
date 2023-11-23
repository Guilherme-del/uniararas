/*
*****************************************************************************
1.Escreva um programa que leia o raio (r) de uma circunferência, e após, imprima o seu
diâmetro (d), o comprimento da circunferência (c) e a área do círculo (a). Utilize a constante
3,14159 para o valor de PI. Dados:
O programa deverá realizar os cálculos mostrados na imagem se o valor do raio for maior
que zero. Caso contrário, deve terminar (return 0;) sem exibir mensagem alguma.
******************************************************************************
*/

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    double raioDaCircunferencia,diametroDaCircunferencia,comprimentoDaCircunferencia,areaDaCircunferencia;

    cout << "Qual o raio da circunferencia ?";
    cin >> raioDaCircunferencia;
    if (raioDaCircunferencia > 0 ) {

    diametroDaCircunferencia = 2*raioDaCircunferencia;
    comprimentoDaCircunferencia = 2*M_PI*raioDaCircunferencia;
    areaDaCircunferencia = M_PI*pow(raioDaCircunferencia,2);

    cout << "O diametro : " << diametroDaCircunferencia << " , comprimento da circunferencia: " << comprimentoDaCircunferencia << " e a area da circunferencia é: "<< areaDaCircunferencia;

    }
    else {
        return 0;
    }
    

    return 0;
}
