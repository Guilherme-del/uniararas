/*
7. O valor de uma conta de energia é dado em função do número de quilowatt/hora, o qual
atualmente custa R$ 0,31. Supondo que em uma casa exista um chuveiro de 5 quilowatt e
que ele fique ligado por uma hora ao dia, faça um programa que leia o número de dias em
que o chuveiro é ligado e calcule o custo total, em reais, de energia gasta. O programa deve
informar o seguinte alerta:
*/

#include <iostream>
#include <cmath>

using namespace std;


int main()
{
    cout<<"Calculando o valor da conta de força!";
    cout<<"Insira o número de dias que o chuveiro é ligado:"<<endl;
    int dias;
    cin>>dias;
   
    float consumo = 5*(1*dias);
   
   
   
    float valor = consumo*0.31;
   
   
    if (valor > 100){
        cout<<"Custo de energia muito elevado!"<<endl;
       
    }
    else{
        cout<<"Custo de energia padrão!"<<endl;
    }
   
    cout<<"Consumo em kWh: "<<consumo<<endl;
    cout<<"Valor consumo: "<<valor<<"R$";
    return 0;
}
