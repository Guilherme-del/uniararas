#ifndef _empresa_h_
#define _empresa_h_

#include <iostream>
#include <vector>
#include "funcionario.h"

using namespace std;

class Empresa
{

private:
	string razaosocial;	
	vector<Funcionario *> listaFuncionarios; // Agora armazenamos ponteiros

public:
	Empresa(string razaosocial);

	void listarFuncionarios();
	void calcularFolhaPagto();
	void contratarFuncionario(Funcionario *f);
	void demitirFuncionario(string codigo);
	void exibirFuncoesFuncionarios();
	void listarFuncionarios();
};
#endif // !_empresa_h_ ;