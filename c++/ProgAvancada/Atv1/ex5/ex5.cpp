/*
5. Modifique o exercício 4 seguindo o seguinte raciocínio: Exiba uma única mensagem no
console pedindo para que o usuário digite, um a um, os três segundos regressivos. Após ler
os três números, exiba em uma única mensagem a contagem (utilizando um único comando
print).
*/

#include <iostream>
#include <Windows.h>

using namespace std;

int main()
{
  int contador;

  cout << "Digite a contagem regressiva de 3 segundos: ";
  cin >> contador;

  for (contador = 3; contador >= 0;contador--)
  {
    cout << contador << endl;
    Sleep(1000);
  }

  return 0;
}