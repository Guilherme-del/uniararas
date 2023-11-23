/*
*****************************************************************************
O lançamento horizontal de um móvel é dado por duas componentes (x e y). As
equações de ambas as componentes são dadas a seguir:
Em que: x0 é a coordenada x inicial, yo é a altura inicial, v0 é a velocidade de lançamento, g
é a aceleração da gravidade e t é o tempo. Faça um programa que calcule a posição do
corpo (componentes x e y) após decorridos t segundos. O programa deve informar erro se y
e t forem negativos.
******************************************************************************
*/



#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    double x,t,y;
    float g;
    g = 9.8;
    cout << "De o valor em segundos de t : ";
    cin >> t;
    
    

    if (y < 0 || t < 0) {
        cout << "ERRO, t E y NEGATIVOS " ;
    }
    else {
      x = 0 + 0 * t;
      y = (g* pow(t,2)/2);
      cout << "O valor de x é : " << x << endl;
      
      cout << "O valor de y : " << y << endl ;
      
    }
    return 0;
}