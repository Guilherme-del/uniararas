/*
3) Crie uma classe em c++ chamada retangulo que armazena as coordenadas cartesianas dos quatros 
cantos do retangulo.
O construtor chama uma função set que recebe quatro conjuntos de coordenadas e verifica se cada um deles esta no primeiro quadrante sem que nenhum valor de coordenada x ou y seja maior que 20. A função set também verifica se as coordenadas fornecidas de fato especificam um retangulo. As funções membro calculam o comprimento , largura , perimetro e area. O comprimento é maior das duas dimensões.
Inclua uma função predicado quadrado que determina se o retangulo é um quadrado.
*/

#include <iostream>
#include <string>
#include <vector>

using namespace std;

class retangulo
{
	float larg, comp, area, perim;
	public:
    retangulo(float L, float C);
    retangulo();
	void define_ret(float L, float C);
    void escreve_tela();
 };
  retangulo::retangulo(float L, float C)
 {
    larg = L;
    comp = C;
    area = larg * comp;
    perim = 2 * (larg + comp);
  }

   retangulo::retangulo()
 {
      larg = comp = area = perim = 0;
 }

   void retangulo::define_ret(float L, float C)
   {
      larg = L;
      comp = C;
      area = larg * comp;
      perim = 2 * (larg + comp);
 }

  void retangulo::escreve_tela()
 {
       cout << "---------------------------------" << endl;
       cout << "Largura = " << larg << endl;
       cout << "Comprimento = " << comp << endl;
       cout << "Area = " << area << endl;
       cout << "Perimetro = " << perim << endl;
       cout << "---------------------------------" << endl;
 }

 int main()
 {
    retangulo r1(2.0, 3.4);
    retangulo r2;

     cout << "---------------------------------" << endl;
     cout << "r2 no inicio do codigo:\n";
     r2.escreve_tela();
     r2.define_ret(10, 20);
     cout << "r2 atualizado:\n";
      r2.escreve_tela();
      cout << "r1:\n";
      r1.escreve_tela();
      return 0;
}
