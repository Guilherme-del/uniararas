/*
7. Faça um programa que mostre na tela todos os múltiplos de 5 no intervalo entre
0 e 100. Use um contador para este fim.
 */
#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{
  for (int i = 0; i <= 100; i = i + 5)
  {
    cout << (i) << endl;
  }
}