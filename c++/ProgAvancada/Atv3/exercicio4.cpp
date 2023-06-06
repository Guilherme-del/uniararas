/*

    4.Faça um programa que leia as medidas do raio e da altura de um recipiente cilíndrico e
    calcule e apresente o volume do recipiente por meio da fórmula:

    vol = 3.14*raio*raio*altura

    Verifique se o valor do volume é negativo; se isso acontecer, o programa deve mostrar um
 alerta:
    Volume negativo, verifique os valores!

*/

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
  double raio, altura, vol;

  cout << "Digite um valor para o raio: ";
  cin >> raio;

  cout << "Digite um valor para a altura: ";
  cin >> altura;

  if (raio < 0 or altura < 0)
  {
    cout << "Volume negativo, verifique os valores!";
  }

  else
  {

    vol = 3.14 * pow(raio, 2) * altura;

    cout << "O volume é: " << vol;
  }
}
