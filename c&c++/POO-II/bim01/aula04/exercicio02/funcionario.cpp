#include "funcionario.h"

Funcionario::Funcionario(string nome, string sb, string cargo, string codigo, double s)
{
	this->Nome = nome;
	this->Sobrenome = sb;
	this->Cargo = cargo;
	this->Salario = s;
	this->Codigo = codigo;
}

string Funcionario::getCargo() {
	return this->Cargo;
}

string Funcionario::getNome() {
	return this->Nome;
}

double Funcionario::getSalario() {
	return this->Salario;
}

void Funcionario::executarFuncao() {
	cout << "Executando uma funcao de funcionario" << endl;
}

Professor::Professor(string nome, string sobrenome, string cargo, string codigo, double sa)
	: Funcionario(nome, sobrenome, cargo, codigo, sa)
{
}

void Professor::executarFuncao() {
	cout << "O professor esta lecionando a disciplina de OO" << endl;
}

Tecnico::Tecnico(string nome, string sobrenome, string cargo, string codigo, double sa)
	: Funcionario(nome, sobrenome, cargo, codigo, sa)
{
}

void Tecnico::executarFuncao() {
	cout << "O tecnico esta trabalhando na infraestrutura do lab" << endl;
}