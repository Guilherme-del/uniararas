/*
18. Faça um programa que receba "N+1" números e mostre a mensagem de valor
positivo, negativo ou zero para cada número. Ao final, o programa deve exibir
na tela a soma dos valores negativos.
*/
#include <iostream>

using namespace std;

int main()
{
  int qtdeValores;
  float somaValores;
  cout << "Quantos valores deve ter aqui?" << endl;
  cin >> qtdeValores;

  int vetor[qtdeValores];

  for (int i = 0; i < qtdeValores; i++)
  {
    cout << "Entre um valor?" << endl;
    cin >> vetor[i];
    if (vetor[i] < 0)
    {
      somaValores += vetor[i];
    }
  }
  cout << somaValores;

  return 0;
}