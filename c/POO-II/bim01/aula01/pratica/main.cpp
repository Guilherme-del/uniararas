/*
1. Crie uma classe para representar uma pessoa, 
   com os atributos privados de nome, idade e altura. 
   Crie os métodos públicos necessários para sets e gets e 
   também um métodos para imprimir os dados de uma pessoa.
*/
#include <iostream>
#include "Funcionario.h"

using namespace std;

int main() {
    /*Instanciando um objeto estático do tipo Funcionario!*/
    Funcionario pessoa;
    /*Métodos que foram definidos dentro da classe PESSOA e herdados*/
    pessoa.setNome();
    pessoa.setIdade();
    pessoa.setAltura();
    pessoa.visualizarDados();
    /*Métodos que foram definidos dentro da classe FUNCIONARIO!*/
    pessoa.setDepartamento();
    pessoa.setSalario();

    return 0;
}