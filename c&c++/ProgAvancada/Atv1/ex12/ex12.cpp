/*
Crie um programa capaz de elevar um número à quinta potência. Exiba o resultado final
no console.
*/

#include <iostream>
#include <math.h>

using namespace std;

int main(){
   float numero;
    
    cout << "Digite um número: ";
    cin >> numero;
    
    cout << "A quinta potencia desse número e: " << (pow(numero,5));
}