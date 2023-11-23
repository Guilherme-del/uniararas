#include <iostream>
using namespace std;

int main()
{
  int x, y, *ponteiroInicial;   // tipo inteiro ocupa 4 endereços de memoria.
  float z, *ponteiroFloat = &z; // Dizemos que ponteiroFloat APONTA "Z"
  char c[2];

  // Ponteiro para tipos inteiros
  ponteiroInicial = &x;  // variavel ponteiroInicial armazenará o endereço da variavle "x";
  *ponteiroInicial = 10; // Atribuição indireta...

  cout << &x << endl
       << &y << endl
       << &z << endl
       << &c << endl
       << "Armazenou o endereço de x: " << ponteiroInicial << endl
       << "Armazenou o endereço de z: " << ponteiroFloat << endl
       << "Conteudo de x: " << x << endl;

  ponteiroInicial = &y;  // agora ponteiroInicial APONTA para o "Y"
  *ponteiroInicial = 20; // e o conteudo da variavel apontada por ponteiroInicial(y) vale 20;

  cout << "Armazenou o endereço de (y) agora: " << ponteiroInicial << endl
       << "Conteudo de y:" << y << endl;
}                                                                                                                                                                                             
