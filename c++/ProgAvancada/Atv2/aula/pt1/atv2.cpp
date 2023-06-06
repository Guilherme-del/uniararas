/******************************************************************************

Atividade executada em aula

*******************************************************************************/

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
  double f, angulo, fx, fy, anguloRad;

  cout << "Digite o modulo da força e o angulo com o eixo x : ";
  cin >> f >> angulo;
  anguloRad = angulo * M_PI / 180;

  fx = f * cos(anguloRad);
  fy = f * sin(anguloRad);

  cout << "componente x =  " << fx <<  " N." << endl;
  cout << "componente y = " << fy << " N" << endl;

  return 0;
}