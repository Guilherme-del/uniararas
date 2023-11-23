/*
20. Faça um programa que pergunte ao usuário em que ano ele nasceu e em que
ano ele está, e mostre de forma progressiva todos os anos que ele já viveu. Obs.:
Valores negativos não são aceitos.
*/

#include <iostream>
#include <ctime>

using namespace std;

int main()
{
  int anoNascimento,idadePessoa = 0;

  time_t t = time(NULL);
  tm *timePtr = localtime(&t);

  cout << "Em qual ano você nasceu ?" << endl;
  cin >> anoNascimento;
  if (anoNascimento > 0)
  {
    for (int i = anoNascimento; i < timePtr->tm_year + 1900; i++)
    {
      cout << "No ano de: " << i << " voce tinha: " << idadePessoa << " ano(s)" << endl;
      idadePessoa += 1;
    }
  }
  else {
    cout << "O ano não pode ser negativo";
    return 0;
  }
  return 0;
}