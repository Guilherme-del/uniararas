/*2. Altere o programa anterior para calcular e apresentar a média dos valores
entrados e aqueles que são maiores e menores que a média..
*/

#include <iostream>
using namespace std;

int main()
{

  double variavel[5], soma, media;

  for (int x = 0; x <= 4; x++)
  {
    cout << "Digite um valor para adicionar a lista: ";
    cin >> variavel[x];
  }

  for (int y = 0; y <= 4; y++)
  {
    soma = soma + variavel[y];
  }

  media = soma / 5;

  cout << "A media é: " << media << endl;

  for (int z = 0; z <= 4; z++)
  {
    if (variavel[z] > media)
    {
      cout << "Valores maiores que a média: " << variavel[z] << endl;
    }
    else if (variavel[z] < media)
    {
      cout << "Valores menores que a média: " << variavel[z] << endl;
    }
  }
}
