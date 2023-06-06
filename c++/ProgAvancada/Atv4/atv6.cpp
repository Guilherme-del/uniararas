/*
6. Faça um programa em que o usuário digite o valor inicial e o valor final da
contagem.
*/
#include <stdio.h>
#include <iostream>

using namespace std;
int main()
{
  int x, y;
  cout << "Digite o valor inicial: " << endl;
  cin >> x;
  cout << "Digite o valor final: " << endl;
  cin >> y;
  if (x < y)
  {
    for (int i = x; i <= y; i++)
    {
      cout << i << endl;
    }
  }
  else if (x > y)
  {
    for (int i = x; i >= y; i--)
    {
      cout << (i) << endl;
    }
  }
  else {
    cout << x ;
  }
}
