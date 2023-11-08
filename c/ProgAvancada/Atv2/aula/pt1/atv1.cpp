/******************************************************************************

Atividade executada em aula

*******************************************************************************/

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
  double x0, x1, y0, y1, distanciaFinal;

  cout << "Qual seu ponto inicial de ambas coordenadas : ";
  cin >> x0 >> y0;

  cout << "Qual seu ponto final de ambas coordenadas : ";
  cin >> x1 >> y1;

  distanciaFinal = (sqrt(pow(x0-y0,2)+pow(x1-y1,2)));

 cout<< "A distancia entre os pontos e: " << distanciaFinal;
  return 0;
}