/*
*****************************************************************************
Faça um programa que leia um valor em horas e converta tal valor em minutos e
segundos. Exemplo:
Caso o valor da hora lida a partir do teclado seja negativo, zero ou maior que 12, o
programa deverá imprimir na tela:
OBS.: Utilize duas ou mais condições distintas.
******************************************************************************
*/

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    double valorEmHoras,valorEmMinutos;

    cout << "Qual horas deseja converter para minutos ?";
    cin >> valorEmHoras;
    
  
    if ( valorEmHoras > 0 || valorEmHoras == 0  || valorEmHoras < 12) {
    valorEmMinutos = valorEmHoras*60 ;
    cout << "Valor em minutos: " << valorEmMinutos;

    }
    else {
      cout << "O numero de lados do poligono deve ser maior que 2 ";
      return 0;
    }
    return 0;
}
