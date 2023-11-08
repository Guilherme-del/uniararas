/*Questão 01 – Faça um programa que leia 5 valores inteiros, armazeno-os em um vetor, calcule
E apresente a soma destes valores.
*/

#include <iostream>
using namespace std;

int main(){
  double Variavel[5], soma;

  for (int x = 0; x <= 4; x++)
  {
    cout << "Digite um valor para adicionar a lista :";
    cin >> Variavel[x];
  }

  for (int y = 0; y <= 4; y++)
  {
    soma = soma + Variavel[y];
  }

  cout << "O valor da soma é : " << soma;
}