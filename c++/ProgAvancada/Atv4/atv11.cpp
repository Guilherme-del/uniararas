/*
11. Faça um programa que leia três notas – utilizando a estrutura de laço - e mostre,
ao final, a respectiva média. Além disso, verifique se o aluno está reprovado
(média menor que 3), de recuperação (média entre 3 e 4.9) ou aprovado (média
igual ou maior a 5).
*/
#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{

  double nota1, nota2, nota3, media;
  int x = 1, avaliacao;

  for (int x = 1; x <= 3; x++)
  {
    cout << "Digite o Valor da Nota: " << endl;
    cin >> avaliacao;

    if (x == 1)
      nota1 = avaliacao;
    else if (x == 2)
      nota2 = avaliacao;
    else
      nota3 = avaliacao;
  }
  media = (nota1 + nota2 + nota3) / 3;

  if (media < 3)
    cout << "Reprovado!";
  else if (media > 3 and media <= 4.9)
    cout << "Recuperação";
  else
    cout << "Aprovado!";

  return 0;
}