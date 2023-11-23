/**************************

                              6. Crie uma agenda eletrônica capaz de realizar a leitura dos dados de uma pessoa física
(Nome completo, RG, CPF, celular, e-mail). Para cada dado, exiba uma frase
autoexplicativa no console. Após realizar a leitura dos dados, imprima todos no console;
logo após, peça ao usuário que confirme a ação, digitando SIM ou NÃO.

***************************/

#include <iostream>

using namespace std;

int main()
{
   int cpf;
   int rg;
   int numeroCel;
   string nome;
   string email;
   
   cout << "Digite Seu nome: ";
   cin >> nome;
   
   cout << "Digite seu número: ";
   cin >> numeroCel;
   
   cout << "Digite seu E-mail: ";
   cin >> email;
   
   cout << "Digite seu CPF: ";
   cin >> cpf;
   
   cout << "Digite seu RG: ";
   cin >> rg;
   
   cout << "Nome: " << nome << " Número: " << numeroCel << " E-mail: " << email << " CPF: " << cpf << " RG: " << rg;
    return 0;
}