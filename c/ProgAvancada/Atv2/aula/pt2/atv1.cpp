/******************************************************************************

                   Aula Pt2. 21/03/2022

*******************************************************************************/

#include <iostream>

using namespace std;

int main()
{
  float n1, n2, mediaFinal;
  cout << "Digite a n1 e a n2: ";
  cin >> n1 >> n2;

  mediaFinal = (n1 + n2 * 3) / 3;

  cout << "Sua media final é: " << mediaFinal << endl;

  if (mediaFinal >= 5)
  {
    cout << "e voce passou !!!";
  }
  else if (mediaFinal >= 3 && mediaFinal < 5)
  {
    cout << "voce esta de RE" << endl;
  }
  else
  {
    cout << "Voce esta reprovado" << endl;
  }
  return 0;
}
