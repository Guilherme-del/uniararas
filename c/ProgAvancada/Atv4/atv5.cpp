/*
5. Faça um programa em que o usuário digite o valor final da contagem e o
programa conte de 0 até o valor escolhido, de maneira progressiva.
*/

#include <stdio.h>
#include <iostream>

using namespace std;
int main()
{
  int x;
  cout << "Digite o valor final da contagem: "<< endl;
  cin >> x;

  for (int i = 0; i != x + 1; i++)
  {
    cout << (i) << endl;
  }
}