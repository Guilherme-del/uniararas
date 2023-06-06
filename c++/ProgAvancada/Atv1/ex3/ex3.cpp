/**************************

3.Faça um programa capaz de realizar a leitura, de forma individual, de uma hora qualquer,
minuto e segundo, respectivamente. Em seguida, exiba no console seguindo o padrão a
seguir.
***************************/

#include <iostream>

using namespace std;

int main()
{
   int hora;
   int minuto;
   int segundo;
   
   cout << "Digite a hora.";
   cin >> hora;
   
   cout << "Digite os minutos.";
   cin >> minuto;
   
   cout << "Digite os Segundos.";
   cin >> segundo;
   
   cout << hora << " horas " << minuto << "minutos" << segundo << " segundos";
   
    return 0;
}