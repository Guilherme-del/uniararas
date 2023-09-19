#include "Pais.h"

Pais::Pais()
{
	this->nome = "";
	this->codigo = "";
	this->kmQuadrado = 0;
	this->populacao = 0;
}

/*definindo a funcao vector*/
Pais::Pais(string nome, string codigo, double dimensao) {
	cout << "Chamada do ctor Pais" << endl;
	
	this->nome = nome;
	this->codigo = codigo;
	this->kmQuadrado = dimensao;
}

/*definindo a fun��o ctor*/
Pais::Pais(string nome, string codigo, double dimensao, vector<Pais> fronteira) 
{
	cout << "Chamada do ctor Pais" << endl;
	this->nome = nome;
	this->codigo = codigo;
	this->kmQuadrado = dimensao;
	this->paisesFronteira = fronteira;
}

void Pais::setCodigo(string codigo) {
	this->codigo = codigo;
}

string Pais::getCodigo() {
	return this->codigo;
}

void Pais::setNome(string nome) {
	this->nome = nome;
}

string Pais::getNome() {
	return this->nome;
}

double Pais::getDimensao() {
	return this->kmQuadrado;
}

void Pais::setDimensao(double dimensao) {
	this->kmQuadrado = dimensao;
}

double Pais::getPopulacao() {
	return this->populacao;
}

void Pais::setPopulacao(double pop) {
	this->populacao = pop;
}

bool Pais::fazFronteira(Pais p) {
	/*percorrer a lista de paises e verificar se h� um de c�digo igual ao pais p*/
	for (Pais pais : this->paisesFronteira) {
		if (pais.codigo == p.codigo)
			return true;
	}	
	return false;
}

double Pais::densidade()
{
	return this->populacao / this->kmQuadrado;
}

void Pais::checarVizinhos(Pais paisCheck)
{
	/*percorrer a lista de paises se h� paises vizinhos*/
	for (Pais pais : this->paisesFronteira)
	{
		for (Pais p : paisCheck.paisesFronteira) 
		{
			if (pais.codigo == p.codigo) {
				cout << "O pais " << this->nome << " eh vizinho de " << p.codigo << endl;
			}
		}
	}
}

void Pais::addVizinho(Pais p) 
{
	if (!this->fazFronteira(p))
		this->paisesFronteira.push_back(p);

}

void Pais::exibirPaisFronteira() {
	for (Pais p : this->paisesFronteira) {
		cout << " | " << p.getNome() << " | " << endl;
	}
}