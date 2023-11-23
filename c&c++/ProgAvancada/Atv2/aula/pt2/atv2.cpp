/******************************************************************************

                   Aula Pt2. 21/03/2022

*******************************************************************************/

#include <iostream>

using namespace std;

int main()
{
  float h, b, areaFinal;
  cout << "Digite a altura: ";
  cin >> h;
  if (h <= 0)
  {
    cout << endl
         << " A altura digitada é negativa!" << endl;
    return 0; // entrada errada programa finaliza com return 0;
  }
  cout << "Digite a base: ";
  cin >> b;
  if (b <= 0)
  {
    cout << endl
         << " A base digitada é negativa!" << endl;
    return 0;
  }

  areaFinal = b*h;
  cout << "Sua area e de: " << areaFinal;
  return 0;
}
