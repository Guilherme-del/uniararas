/*
*****************************************************************************
9.A cidade A possui 90.000 habitantes e a cidade B, 50.000. A população da cidade A
cresce 0,9% ao ano, enquanto que a da cidade B cresce 1,5% ao ano. Faça um programa
que leia o número de anos e o número estimado da população de cada cidade. O programa
deve verificar se a população da cidade A é maior que a da cidade B ou se a população da
cidade B é maior que a da cidade A.
******************************************************************************
*/

#include <iostream>
#include <cmath>

using namespace std;

int main()
{

  double habitantesEmA, habitantesEmB, crescimentoCidadeA, crescimentoCidadeB, numeroDeAnos, numeroDeHabitantes, valorDoCrescimentoDeA, valorDoCrescimentoDeB, qtdeA, qtdeB;
  cout << "Quantos Anos se passaram? ";
  cin >> numeroDeAnos;

  habitantesEmA = 90.000;
  habitantesEmB = 50.000;

  crescimentoCidadeA = 0.9;
  crescimentoCidadeB = 1.5;

  valorDoCrescimentoDeA = ((habitantesEmA * crescimentoCidadeA) / 100) * numeroDeAnos;
  valorDoCrescimentoDeB = ((habitantesEmB * crescimentoCidadeB) / 100) * numeroDeAnos;

  qtdeA = habitantesEmA + valorDoCrescimentoDeA;
  qtdeB = habitantesEmB + valorDoCrescimentoDeB;

  if (qtdeA > qtdeB)
  {

    cout << "A cidade A e maior que B, contendo: " << qtdeA << " mil habitantes "
         << " ja a cidade B possui " << qtdeB << " habitantes";
  }
  else if (qtdeB > qtdeA)
  {
    cout << "A cidade B e maior que A, contendo: " << qtdeB << " mil habitantes"
         << " ja a cidade A possui " << qtdeA << " habitantes";
  }

  return 0;
}
