/*
5. O índice de massa corpórea (IMC) é:
No qual a altura é dada em metros e o peso é dado em quilogramas. Considerando isso,
faça um programa que calcule o IMC da pessoa, cujo valor ideal está entre 18,5 e 24,9. O
programa deve alertar o usuário:
*/


#include <iostream>
#include <cmath>

using namespace std;


int main()
{    
    float imc, peso, altura;
    
    cout << "Digite seu peso: ";
    cin>>peso;
    
    cout<<"Digite sua altura em metros: ";
    cin>>altura;
    
    imc = peso/pow(altura, 2);
    
    if (imc < 18.5) {
        cout<<"Seu IMC está abaixo do ideal";
    }
       
    else if (imc > 24.9){
        cout<<"Seu IMC está acima do ideal";
    };
    

    return 0;
}

