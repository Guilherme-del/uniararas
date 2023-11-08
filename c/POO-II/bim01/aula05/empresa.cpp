#include "empresa.h"
#include "funcionario.h"

Empresa::Empresa(string razaosocial)
{
	this->razaosocial = razaosocial;
}

void Empresa::listarFuncionarios()
{
	if (listaFuncionarios.empty())
	{
		std::cout << "Não há funcionários na empresa." << std::endl;
	}
	else
	{
		std::cout << "Funcionários da empresa " << razaosocial << ":" << std::endl;
		for (Funcionario *f : listaFuncionarios)
		{
			std::cout << f->getNome() << std::endl;
		}
	}
}

void Empresa::calcularFolhaPagto()
{

	double total = 0;

	for (Funcionario *f : this->listaFuncionarios)
	{
		total += f->getSalario();
		cout << f->getNome() << " | " << f->getCargo() << endl;
	}

	cout << "O total da folha de pagto eh: " << total << endl;
}

void Empresa::contratarFuncionario(Funcionario *f)
{
	this->listaFuncionarios.push_back(f);
}

/*Polimorfismo em acao!*/
void Empresa::exibirFuncoesFuncionarios()
{
	for (Funcionario *f : this->listaFuncionarios)
	{
		cout << f->getNome() << " | " << endl;
		f->executarFuncao(); // Use -> para chamar a função em um ponteiro
	}
}

void Empresa::demitirFuncionario(std::string codigo)
{
	int index = -1;

	// Procurar o índice do funcionário com o código especificado
	for (size_t i = 0; i < listaFuncionarios.size(); ++i)
	{
		if (listaFuncionarios[i]->getCodigo() == codigo)
		{
			index = static_cast<int>(i);
			break;
		}
	}

	if (index != -1)
	{
		// Funcionário encontrado, demitir
		delete listaFuncionarios[index];
		listaFuncionarios.erase(listaFuncionarios.begin() + index);
		std::cout << "Funcionário com código " << codigo << " demitido com sucesso." << std::endl;
	}
	else
	{
		std::cout << "Funcionário com código " << codigo << " não encontrado." << std::endl;
	}
}