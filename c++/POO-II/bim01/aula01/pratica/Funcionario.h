/*O #ifndef Garante que não haverá duplicidade na hora de "usar" o arquivo ao longo da compilação/execução. 
  Evita duplicar tipos, e demais estruturas presentes.
  É UMA BOA PRÁTICA NA PROGRAMAÇÃO OOP EM C++.
*/
#ifndef _FUNCIONARIO_H_
#define _FUNCIONARIO_H_

#include <iostream>
#include "Pessoa.h"

using namespace std;

/*A classe funcionário
    HERDA atributos e métodos da classe Pessoa.
    Por padrão, herança é PRIVADA, por isso devemos explicitar
    "public" antes da classe Pessoa.
*/
class Funcionario : public Pessoa
{
private:
    string Funcao;
    string Departamento;
    float Salario;

public:
    Funcionario(); //construtor default - pode ser omitido
    void setFuncao();
    string getFuncao();
    void setDepartamento();
    string getDepartamento();
    void setSalario();
    float getSalario();
};

#endif