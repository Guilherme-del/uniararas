/*
17. Faça um programa que seja capaz receber N valores fornecidos pelo usuário e
exiba na tela o valor da multiplicação dos valores pares.
*/
#include <iostream>

using namespace std;

int main()
{
  int qtdeValores;
  float alunoNota, mult;

  cout << "Quantos valores deseja inserir ?" << endl;
  cin >> qtdeValores;
  int vetor[qtdeValores], newArray[qtdeValores];

  for (int i = 0; i < qtdeValores; i++)
  {
    cout << "Entre um valor?" << endl;
    cin >> vetor[i];
  }
  int x = 0;
  for (int j = 0; j < qtdeValores; j++)
  {
    if (vetor[j] % 2 == 0)
    {
      newArray[x]; // armazena os valores pares
      x++;
    }
  }
  for (int y = 0; y < qtdeValores; y++)
  {
    if (newArray[y] != 0)
    {
      if (y = 0)
      {
        mult = newArray[y];
      }
      else
      {
        mult = mult * newArray[y];
      }
    }
  }
  cout << mult;

  return 0;
}