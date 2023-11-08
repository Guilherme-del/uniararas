/*
2. Faça um programa capaz de realizar a leitura, de forma individual, do dia, mês e ano
atual; utilize Imprima no console os respectivos inputs
 */

#include <iostream>
using namespace std;

int main()
{
    int diaSemana;
    int initialMes;
    int initialAno;

    cout << "Digite o dia? " << endl;
    cin >> diaSemana;
    cout << "Qual o mês ?" << endl;
    cin >> initialMes;
    cout << "Qual o ano ?" << endl;
    cin >> initialAno;

    cout << diaSemana << "/" << initialMes << "/" << initialAno;

    return 0;
}
