/*
15. Escreva um programa que pergunte ao usuário quantos alunos tem na sala dele.
Em seguida, peça ao usuário para que entre com as notas de todos os alunos da
sala, e, para cada aluno, o programa imprime se ele está aprovado ou reprovado.
*/

#include <iostream>

using namespace std;

int main()
{
  int qtdeAlunos;
  float alunoNota;

  cout << "Quantos alunos tem na sua sala ?" << endl;
  cin >> qtdeAlunos;
  int *vetor = new int[qtdeAlunos];

  for(int i = 0; i < qtdeAlunos; i++) {
    cout << "Qual a nota deste aluno ?" << endl;
    cin >> vetor[i];
    if (vetor[i] < 5) {
      cout << "Aluno reprovado" << endl;
    }
    else {
      cout << "Aluno aprovado" << endl;
    }
  }

  return 0;
}