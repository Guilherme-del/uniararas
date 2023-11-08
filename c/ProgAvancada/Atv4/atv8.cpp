/*
8. Faça um programa que represente uma bomba, o qual deve começar no tempo
de 1 minuto e decrementar até 0. Quando o valor for menor que zero, o
programa deve imprimir na tela:
*/
#include <stdio.h>
#include <iostream>
#include <unistd.h>

using namespace std;

int main()
{
  for (int i = 60; i >= -1; i--)
  {
    if (i < 0)
    {
      cout << "################" << endl
           << "     BOOOOM" << endl
           << "################" << endl;
    }
    else if (i >= 0)
    {
      cout << (i) << endl;
      sleep(1);
    }
  }
}
