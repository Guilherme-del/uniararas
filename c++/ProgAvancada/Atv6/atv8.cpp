/*8. Faça um programa que calcule a trajetória de um móvel em movimento uniforme
do instante 0 até o instante 10. Armazene cada valor da posição em um vetor.
Assume que cada posição do vetor corresponda a um instante de tempo.
*/
#include <iostream>
using namespace std;

int main()
{


    int QuantidadeLista = 10;
    double PosicaoInicial, VelocidadeInicial, PosicaoFinal;
    double Vetor1[QuantidadeLista], Vetor2[QuantidadeLista];
    
    cout << "Digite um valor para a Posicao Inicial: " << endl;
    cin >> PosicaoInicial;
    
    cout << "Digite um valor para a Velocidade Inicial: " << endl;
    cin >> VelocidadeInicial;
    
    // Instante de tempo
    // MVU = So + Vo.t
    
    for (int w = 0; w <= (QuantidadeLista-1); w++) {
        Vetor1[w] = w;
    }
    
    for (int y = 0; y <= (QuantidadeLista-1); y++) {
        PosicaoFinal = PosicaoFinal + VelocidadeInicial*Vetor1[y];
        Vetor2[y] = PosicaoFinal;
    }
    
    for (int z = 0; z <= (QuantidadeLista-1); z++) {
        cout << "O valor para t " << z << " é: " << Vetor2[z] << endl;
    }
}