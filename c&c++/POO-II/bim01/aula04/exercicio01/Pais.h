#ifndef Exercicio_1_Pais
#define Exercicio_1_Pais

#include <iostream>
#include <vector>

using namespace std;

class Pais {

private:
	string nome;
	string codigo;
	double kmQuadrado;
	double populacao;
	vector<Pais> paisesFronteira; //Configura uma agregação
public:
	//construtor da classe que possui parâmetros
	Pais();
	Pais(string nome, string codigo, double dimensao);
	Pais(string nome, string codigo, double dimensao, vector<Pais> fronteira);
	//set
	void setNome(string nome);
	void setCodigo(string codigo);
	void setPopulacao(double pop);
	void setDimensao(double dimensao);
	//get
	string getNome();
	string getCodigo();
	double getPopulacao();
	double getDimensao();
	//custom
	bool fazFronteira(Pais p);
	double densidade();
	void checarVizinhos(Pais p);
	void addVizinho(Pais p);

	void exibirPaisFronteira();
};

#endif // !pais_h