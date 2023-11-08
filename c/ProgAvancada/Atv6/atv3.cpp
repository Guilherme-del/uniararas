/*3. Faça um programa que leia 10 valores reais e os apresente na ordem inversa
entrada.*/
#include <iostream>
using namespace std;

int main()
{
  int QuantidadeLista = 10;
  double Variavel[QuantidadeLista];

  for (int x = 0; x <= (QuantidadeLista - 1); x++)
  {
    cout << "Digite um valor para adicionar a lista: ";
    cin >> Variavel[x];
  }

  for (int y = (QuantidadeLista - 1); y >= 0; y--)
  {
    cout << "Valor: " << Variavel[y] << endl;
  }
}
