/*9. Dada uma sequência de 8 números lidos do teclado, imprimi-la na ordem inversa
à da leitura.
*/
#include <iostream>
using namespace std;

int main()
{
  int QuantidadeLista = 8;
  double Vetor1[QuantidadeLista];

  for (int x = 0; x <= (QuantidadeLista - 1); x++)
  {
    cout << "Digite um vlaor para incluir ao vetor: ";
    cin >> Vetor1[x];
  }
  for (int y = (QuantidadeLista - 1); y >= 0; y--)
  {
    cout << "Valor: " << Vetor1[y] << endl;
  }
}