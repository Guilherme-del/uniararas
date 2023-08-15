/*Precisamos incluir o arquivo de cabeçalho da nossa classe Funcionario
  Assim temos como acessar os atributos/métodos públicos.
*/
#include "Funcionario.h"

/*Definição - implementação - dos métodos que foram assinados no arquivo Funcionario.h*/

Funcionario::Funcionario()
{
    cout << "Chamada do ctor Funcionario\n" << endl;
}

void Funcionario::setFuncao()
{
    cin >> this->Funcao;
}

string Funcionario::getFuncao()
{
    return this->Funcao;
}

void Funcionario::setDepartamento()
{
    cout << "Informe o depatamento: " << endl;
    cin >> this->Departamento;
}

string Funcionario::getDepartamento()
{
    return this->Departamento;
}

void Funcionario::setSalario()
{
    cout << "Informe o salario: " << endl;
    cin >> this->Salario;
}

float Funcionario::getSalario()
{
    return this->Salario;
}