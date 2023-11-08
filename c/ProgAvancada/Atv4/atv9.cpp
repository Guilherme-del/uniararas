/*
9. Faça um programa que conte progressivamente de 0 até 1.000 e depois conte
regressivamente de 1.000 até 0.
*/
#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{

  for (int x = 0; x <= 1000; x++)
  {
    cout << "Valor de X: " << x << endl;
    if (x == 1000)
    {
      for (int y = 1000; y >= 0; y--)
      {
        cout << "Valor de Y: " << y << endl;
      }
    }
  }
  return 0;
}