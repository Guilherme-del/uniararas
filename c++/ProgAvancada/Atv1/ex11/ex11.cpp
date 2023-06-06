/*
11 um programa em Python capaz de realizar a contagem regressiva partindo do
número 5. Diferentemente do exercício da seção anterior, use apenas uma única variável
chamada “contagem”, que inicia em 5. Atualize o valor da variável pedindo ao usuário para
digitar os próximos números da contagem, exibindo o valor no console.
*/
#include <iostream>

using namespace std;

// sua contagem começa em 5

int main(){
 
    // sua contagem começa em 5
    
    int contagem,num1,num2,num3,num4;
    
    contagem = 5;
    
    cout << "Sua contagem começa em: " << contagem << endl;
    
    cout << "Digite os seguintes quatros numeros!" << endl;
    
    cout << "Numero: ";
    cin >> num1;
    
    cout << "Numero: ";
    cin >> num2;
    
    cout << "Numero: ";
    cin >> num3;
    
    cout << "Numero: ";
    cin >> num4;
    
    cout << "Contagem regressiva em: " << num1 << endl;
    cout << "Contagem regressiva em: " << num2 << endl;
    cout << "Contagem regressiva em: " << num3 << endl;
    cout << "Contagem regressiva em: " << num4 << endl;
    cout << "Contagem regressiva em: " << "ZERO" << endl;

}