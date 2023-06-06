/*
Atividade MB - Programação Avançada
Exiba a tabuada do 6 na tela usando o comando for. Use um contador de 0 a 10
para essa finalidade.
*/
#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{

  int valorTabuada;
  for (int x = 0; x <= 10; x++)
  {
    valorTabuada = 6 * x;
    cout << "Valor: " << valorTabuada << endl;
  }
  return 0;
}