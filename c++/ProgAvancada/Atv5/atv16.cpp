/*
16.Faça um programa que gere os n primeiros termos de uma PA. Dados como a
entrada, o primeiro termo e a razão (passo).
*/
#include <iostream>

using namespace std;

int main()
{

  int n = 0;
  float a1 = 0.0, r = 0.0, an = 0.0, sn = 0.0;

  cout << "Digite o primeiro termo da PA =>";
  cin >> a1;

  cout << "Digite a razao da PA =>";
  cin >> r;

  cout << "Digite quantos termos serao somados =>";
  cin >> (n);

  an = a1 + (n - 1) * r;
  sn = ((a1 + an) * n) / 2;

  cout << ("\nA soma dos %2d primeiros termos da PA eh %7.3f\n", n, sn);

  return 0;
}