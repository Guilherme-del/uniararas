/*
Faça um programa que leia um número e calcule seu fatorial. Exemplo: 5 foi
lido, então, 1*2*3*4*5 =120.
*/
#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{

  int fatorial;
  int valor = 1;

  cout << "Fatorial: " << endl;
  cin >> fatorial;

  for (int x = fatorial; x >= 1; x--)
  {
    valor = valor * x;
  }

  cout << "Valor: " << valor << endl;
  return 0;
}