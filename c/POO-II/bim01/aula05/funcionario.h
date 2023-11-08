// funcionario.h
#ifndef _funcionario_h_
#define _funcionario_h_

#include <iostream>
#include <string> // Adicione a inclusão para o tipo 'string'

using namespace std;

class Funcionario {
private:
    string Nome;
    string Sobrenome;
    string Cargo;
    string Codigo;
    double Salario;

public:
    Funcionario(string nome, string sobrenome, string cargo, string codigo, double sa);
    
    double getSalario();
    string getNome();
    string getCargo();
    string getCodigo(); // Adicione este método para obter o código do funcionário
    
    virtual void executarFuncao();
};

class Professor : public Funcionario {
public:
    Professor(string nome, string sobrenome, string cargo, string codigo, double sa);
    void executarFuncao();
};

class Tecnico : public Funcionario {
public:
    Tecnico(string nome, string sobrenome, string cargo, string codigo, double sa);
    void executarFuncao();
};

#endif // !_funcionario_h_
