#include "empresa.h"
#include "funcionario.h"

Empresa::Empresa(string razaosocial)
{
	this->razaosocial = razaosocial;
}

void Empresa::calcularFolhaPagto() {

	double total = 0;

	for (Funcionario f : this->listaFuncionarios) {
		total += f.getSalario();
		cout << f.getNome() << " | " << f.getCargo() << endl;
	}

	cout << "O total da folha de pagto eh: " << total << endl;
}

void Empresa::contratarFuncionario(Funcionario f)
{
	this->listaFuncionarios.push_back(f);
}

/*Polimorfismo em acao!*/
void Empresa::exibirFuncoesFuncionarios()
{
	for (Funcionario f : this->listaFuncionarios) {
		cout << f.getNome() << " | " << endl;
		f.executarFuncao();
	}
}