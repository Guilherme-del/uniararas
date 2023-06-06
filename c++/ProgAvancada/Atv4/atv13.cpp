/*
13. Escreva um programa que pergunte um número ao usuário e mostre a tabuada
completa desse número (de 1 até 10).
*/
#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{
  int tabuada, parametro;

  cout << "Tabuada: " << endl;
  cin >> tabuada;

  for (int x = 1; x <= 10; x++)
  {
    parametro = tabuada * x;
    cout << "Valor: " << parametro << endl;
  }

  return 0;
}