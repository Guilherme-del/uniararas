/*
19. Faça um programa que peça para o usuário inserir 20 números e calcule a soma
dos números que forem positivos. Aos números negativos, uma mensagem de
erro deve ser impressa na tela.
*/
#include <iostream>

using namespace std;

int main()
{
  int vetor[20];
  float somaValores;

  for (int i = 0; i <= 3; i++)
  {
    cout << "Digite um valor ?" << endl;
    cin >> vetor[i];
    if (vetor[i] > 0)
    {
      somaValores += vetor[i];
      cout << "Soma dos números positivos até agora: " << endl << somaValores << endl;
    }
    else
    {
      cout << "Número não pode ser negativo" << endl;
    }
  }

  return 0;
}