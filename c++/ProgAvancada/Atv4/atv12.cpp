/*
12. Escreva um programa que leia o tamanho da altura de um retângulo e imprima
um retângulo daquele tamanho com asteriscos. A largura do retângulo é fixa
em 20 asteriscos. Exemplo: Leu 5 de altura.
*/
#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{
  int largura = 20,h;
  char caracter = '*';

  cout << "Digite a h: " << endl;
  cin >> h;

  for (int y = 0; y <= h; y++)
  {
    for (int x = 0; x <= largura; x++)
    {
      cout << caracter;
    }
    cout << endl;
  }

  return 0;
}