/*
8. Suponha que você irá desenvolver um sistema para gerenciar suas notas. O programa
deve conter variáveis para guardar RA, notas N1 e N2, e média. Deve ser capaz de realizar
a leitura desses valores via teclado e, após isso, você deve fazer as conversões
necessárias dos tipos de dados.
Lembre-se que o RA é inteiro e as notas possuem casas decimais (valores reais).
*/

#include <iostream>

using namespace std;

int main()
{
  int numRA;
  float nota1;
  float nota2;
  float mediaSemestre;

  cout << "Digite o numero do RA: ";
  cin >> numRA;
  cout << "Digite a nota 1: ";
  cin >> nota1;
  cout << "Digite a nota 2: ";
  cin >> nota2;

 mediaSemestre = (nota1 + (nota2*2))/3;
 
 cout << "RA: " << numRA << "Media: " << mediaSemestre;

  return 0;
}