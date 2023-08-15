/*Precisamos incluir o arquivo de cabeçalho da nossa classe Pessoa
  Assim temos como acessar os atributos/métodos públicos.
*/
#include "Pessoa.h"

/*Definição - implementação - dos métodos que foram assinados no arquivo Pessoa.h*/

Pessoa::Pessoa()
{
  cout << "Chamada do ctor PESSOA\n";
}

void Pessoa::setNome()
{
  cout << "Informe o nome: " << endl;
  getline(cin, this->Nome); // Realizando a leitura dos dados do teclado
                            // e atribui na variável nome
}

string Pessoa::getNome()
{
  return this->Nome;
}

void Pessoa::setIdade()
{
  cout << "Informe a idade: " << endl;
  cin >> this->Idade;
}

int Pessoa::getIdade()
{
  return this->Idade;
}
void Pessoa::setAltura()
{
  cout << "Informe a altura: " << endl;
  cin >> this->Altura;
}

float Pessoa::getAltura()
{
  return this->Altura;
}

void Pessoa::visualizarDados()
{
  cout << "Nome: " << this->Nome << endl;
  cout << "Idade: " << this->Idade << endl;
  cout << "Altura: " << this->Altura << endl;
}