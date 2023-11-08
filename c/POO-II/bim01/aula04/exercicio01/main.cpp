#include <iostream>

/*1. Escreva uma classe que represente um pa�s.Um pa�s � representado
atraves dos atributos : c�digo(ex.: BRA), nome(ex.: Brasil),
populacao(ex.: 193.946.886) e a sua dimens�o em Km2(ex.:
8.515.767, 049).Al�m disso, cada pa�s mant�m uma lista de outros
paises com os quais ele faz fronteira.Escreva a classe e
forneca os seus membros a seguir :

a) Construtor que inicialize o codigo ISO, o nome e a dimens�o do
pais;
b) Metodos de acesso(getter / setter) para as propriedades c�digo
ISSO, nome, populacao e dimensao do pais;
c) Um metodo que informe se outro pais faz fronteira do pa�s que
recebeu a mensagem;
d) Um metodo que retorne a densidade populacional do pa�s(h / km2);
e) Um metodo que receba um pais como parimetro e retorne a lista de
vizinhos comuns aos dois paises.

Considere que um pa�s tem no m�ximo 5 outros paises com os quais ele
faz fronteira.*/

/*Baseado no exercício do País, modifique-o conforme pede:
Faça um menu que permita o usuário escolher entre as seguintes opções:
1. Criar e adicionar um pais em uma lista de países existentes no main (vector);
2. Adicionar um país na lista de paises fronteira de um país escolhido (use o código);
3. Visualizar a lista de países fronteira de um país escolhido (use o código);
4. Visualizar a densidade de um pais escolhido;
5. Ver quais são os países fronteira em comum dado dois países;
6. Ver se um determinado país é fronteira com outro;
7. Visualizar a lista de países do main (vector);
8. Encerrar o programa;

Faça funções auxiliares no arquivo main para facilitar a manipulação dessa lista
geral.
Crie uma função cabeçalho;
Crie uma função capaz de encontrar um país, dado a lista de paises e o código;

Faça as alterações necessárias no header do Pais para garantir o funcionamento
da aplicação. Implemente utilizando memória estática, e depois modifique para
trabalhar com ponteiros e alocação dinâmica.
*/

#include "Pais.h"

using namespace std;

void cabecalho(int &opcao)
{
  cout << "Digite o numero da opcao: " << endl;
  cout << "1. Criar e adicionar um pais no nosso banco de dados" << endl;
  cout << "2. Adicionar um país na lista de paises fronteira de um país escolhido" << endl;
  cout << "3. Visualizar a lista de países fronteira de um país escolhido(use o código)" << endl;
  cout << "4. Visualizar a densidade de um pais escolhido" << endl;
  cout << "5. Ver quais são os países fronteira em comum dado dois países" << endl;
  cout << "6. Ver se um determinado país é fronteira com outro;" << endl;
  cout << "7. Visualizar a lista de países do main(vector);" << endl;
  cout << "8. Encerrar o programa;" << endl;
  cin >> opcao;
}

Pais *encontrarPais(string codigo, vector<Pais *> baseDeDados)
{
  for (Pais *p : baseDeDados)
  {
    if (p->getCodigo() == codigo)
      return p;
  }

  return NULL;
}

int main()
{
  /*Banco de dados - criando um vector de paises*/
  vector<Pais *> bancoDeDados;

  /*variável auxiliar*/
  int opcao;
  string codigo;

  /*nossa aplicação vai executar até que a opção
  de sair seja informada*/
  while (true)
  {

    cabecalho(opcao);

    if (opcao == 1)
    {

      string nome, codigo;
      double dimensao;

      cout << "Informe o nome do novo pais: " << endl;
      cin >> nome;
      cout << "Informe o codigo do novo pais: " << endl;
      cin >> codigo;
      cout << "Informe a dimensao do novo pais: " << endl;
      cin >> dimensao;

      Pais *novoPais = new Pais(nome, codigo, dimensao);
      bancoDeDados.push_back(novoPais);

      cout << "Pais adicionado com sucesso!" << endl;
    }
    else if (opcao == 2)
    {
      cout << "Informe o codigo do pais para acessar a lista de fronteiras" << endl;
      cin >> codigo;

      /*funcao para procurar um pais no banco de dados*/
      Pais *resultado = encontrarPais(codigo, bancoDeDados);

      if (resultado->getNome() != "")
      {
        cout << "Informe o codigo do pais a ser inserido na lista de fronteiras" << endl;
        cin >> codigo;

        Pais *fronteira = encontrarPais(codigo, bancoDeDados);

        if (fronteira->getCodigo() != "")
        {
          resultado->addVizinho(*fronteira);
          fronteira->addVizinho(*resultado);
        }
        else
          cout << "Pais nao encontrado, por favor, cadastre!" << endl;
      }
    }
    else if (opcao == 3)
    {
      cout << "Informe o codigo do pais para acessar a lista de fronteiras" << endl;
      cin >> codigo;

      Pais *resultado = encontrarPais(codigo, bancoDeDados);

      if (resultado->getNome() != "")
        resultado->exibirPaisFronteira();
    }
    else if (opcao == 4)
    {

      cout << "Informe o codigo do pais" << endl;
      cin >> codigo;

      Pais *resultado = encontrarPais(codigo, bancoDeDados);

      if (resultado->getNome() != "")
        resultado->densidade();
    }
    else if (opcao == 5)
    {
      cout << "Informe o codigo do primeiro pais" << endl;
      cin >> codigo;

      Pais *pais1 = encontrarPais(codigo, bancoDeDados);

      if (pais1->getNome() != "")
      {
        cout << "Informe o codigo do segundo pais" << endl;
        cin >> codigo;

        Pais *pais2 = encontrarPais(codigo, bancoDeDados);

        if (pais2->getNome() != "")
          pais1->checarVizinhos(*pais2);
      }
    }
    else if (opcao == 6)
    {
      cout << "Informe o codigo do primeiro pais" << endl;
      cin >> codigo;

      Pais *pais1 = encontrarPais(codigo, bancoDeDados);

      if (pais1->getNome() != "")
      {
        cout << "Informe o codigo do segundo pais" << endl;
        cin >> codigo;

        Pais *pais2 = encontrarPais(codigo, bancoDeDados);

        if (pais2->getNome() != "")
        {
          if (pais1->fazFronteira(*pais2))
            cout << "Pais 1 faz fronteira com o 2" << endl;
          else
            cout << "Pais não faz fronteira!" << endl;
        }
      }
    }
    else if (opcao == 7)
    {
      cout << "Nosso banco de dados contem: " << endl;
      for (Pais *p : bancoDeDados)
      {
        cout << " | " << p->getNome() << " | ";
      }
    }
    else
    {
      cout << "Encerrando!";
      return 0;
    }
  }
  return 0;
}