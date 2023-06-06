/**5. Faça um programa que leia e armazene dois vetores a e b com 5 elementos cada
e apresente o resultado de:
somatoria 0 - 4
(vetor1[i] + vetor2[4 - i])
*/
#include <iostream>
using namespace std;

int main()
{
  int QuantidadeLista = 5;
  int somatoria;

  double Vetor1[QuantidadeLista], Vetor2[QuantidadeLista];

  for (int w = 0; w <= (QuantidadeLista - 1); w++)
  {
    cout << "Digite um valor para adicionar ao vetor 1: ";
    cin >> Vetor1[w];
  }

  for (int y = 0; y <= (QuantidadeLista - 1); y++)
  {
    cout << "Digite um valor para adicionar ao vetor 2: ";
    cin >> Vetor2[y];
  }

  for (int z = 0; z <= 4; z++)
  {
    somatoria = Vetor1[z] + Vetor2[4 - z];
  }
  cout << "Valor da somatoria: " << somatoria;
}