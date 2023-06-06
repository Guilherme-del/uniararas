/*
Crie um programa capaz de elevar um número à quinta potência. Exiba o resultado final
no console.
*/

#include <iostream>
#include <math.h>

using namespace std;

int main()
{
  {
    // formula = V² = vo² + 2ads

    float v, a, ds, formula;

    cout << "Digite o valor para velocidade inicial: ";
    cin >> v;

    cout << "Digite o valor para aceleracao: ";
    cin >> a;

    cout << "Digite o valor para distancia: ";
    cin >> ds;

    formula = (v * v) + (2 * a) + ds;

    cout << "O valor de V² é: " << formula << endl;
  }
}