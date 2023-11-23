/*
4. Faça um programa capaz de realizar leituras de contagens regressivas, partindo de três
segundos. A cada número inserido pelo usuário, a saída já deve ser exibida logo em
seguida. Supondo que o usuário digitou 3, no console já deve ser exibido “Faltam 3
segundos!!!”, e assim sucessivamente.
*/

#include <iostream>

using namespace std;

int main()
{
  int contador;

  cout << "Digite a contagem.";
  cin >> contador;

  cout << "faltam" << contador << "segundos";

  return 0;
}