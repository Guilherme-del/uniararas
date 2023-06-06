/*
8.Sabendo-se que o latão é constituído de 70% de cobre e 30% de zinco, faça um programa
que leia quantos quilos de latão deseja-se produzir e informe quantos quilos de cobre e
zinco são necessários. Suponha que o material zinco disponível seja 100 kg e o material
cobre seja 50 kg.
*/

#include <iostream>
#include <cmath>

using namespace std;

int main()
{

  double latao, zin, cobre;

  cout << "Qual a quantidade de latão que você deseja produzir: ";
  cin >> latao;

  zin = 100.00;
  cobre = 50.00;

  cout << "Para produzir, " << latao << "KG de latão é necessário: " << endl;
  cout << "Cobre: " << latao * 0.7 << endl;
  cout << "Zinco: " << latao * 0.3 << endl;

  if (latao * 0.7 > zin or latao * 0.3 > cobre)
  {

    cout << "Não há material suficiente!";
  }
  else
  {

    cout << "A quantidade de latão produzida é a de: " << (latao * 0.7 + latao * 0.3) << "KG";
  }
}
