#include <iostream>

using namespace std;

int main(){
    // Calculo: VAR = X² + 3x - 1   
    float x;
    float formula;
    
    cout << "Digite o valor de x: ";
    cin >> x;
    
    formula = (x*x) + (3*x) - 1;
    
    cout << "O valor da formula é: " << formula;
}