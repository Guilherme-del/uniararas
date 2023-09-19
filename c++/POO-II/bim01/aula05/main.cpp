/*
Exercício para prática (Dúvidas, utilizem o chat abaixo):
1)  Com base no código do exercício 2, postado na última aula, realize as seguintes modificações:
	A. Construa um menu com cabeçalho e todas as opções para manipular os funcionários da empresa no programa principal. Seu programa deverá funcionar até que o usuário informe que deseja sair.
	B. Modifique a sua classe Empresa para que haja uma lista de ponteiros de Funcionario. Faça as modificações necessárias nos códigos existentes para a correta execução.
	C. Construa uma função, na classe Empresa, capaz de listar todos os nomes dos funcionários dessa empresa criada. Caso não haja funcionários, exiba uma mensagem informando.
	D. Construa uma função, na classe Empresa, capaz de demitir um funcionário através de código informado. Dica: Utilize a função "erase" da STL vector, para isso você deverá descobrir qual o índice do elemento que deseja remover.
	Exemplo do código: meuVector.erase(meuVector.begin() + indiceElemento);
	Construa o seu programa utilizando ponteiros (tome como base o exercício do País postado, utilize o operador "new"). Faça uso de funções que explorem o polimorfismo.
*/
#include <iostream>
#include "funcionario.h"
#include "empresa.h"

int main()
{
	Empresa emp("FHO");
	// Variável para armazenar a escolha do usuário
	int escolha;

	do
	{
		// Limpa a tela
		system("clear");
		// Exibe o cabeçalho do menu
		std::cout << "===== Menu da Empresa =====" << std::endl;
		std::cout << "1. Contratar Funcionário" << std::endl;
		std::cout << "2. Calcular Folha de Pagamento" << std::endl;
		std::cout << "3. Exibir Funções dos Funcionários" << std::endl;
		std::cout << "4. Listar Funcionario" << std::endl;
		std::cout << "5. Demitir Funcionario" << std::endl;
		std::cout << "6. Sair" << std::endl;
		std::cout << "Digite sua escolha: ";
		std::cin >> escolha;

		switch (escolha)
		{
		case 1:
		{
			// Solicitar informações do funcionário e contratá-lo
			std::string nome, sobrenome, cargo, codigo;
			int horasTrabalhadas;
			std::cout << "Nome: ";
			std::cin >> nome;
			std::cout << "Sobrenome: ";
			std::cin >> sobrenome;
			std::cout << "Cargo: ";
			std::cin >> cargo;
			std::cout << "Código: ";
			std::cin >> codigo;
			std::cout << "Horas Trabalhadas: ";
			std::cin >> horasTrabalhadas;

			Funcionario *novoFuncionario;

			if (cargo == "Professor")
			{
				novoFuncionario = new Professor(nome, sobrenome, cargo, codigo, horasTrabalhadas);
			}
			else if (cargo == "Tecnico")
			{
				novoFuncionario = new Tecnico(nome, sobrenome, cargo, codigo, horasTrabalhadas);
			}
			else
			{
				std::cout << "Cargo não reconhecido." << std::endl;
				break;
			}

			emp.contratarFuncionario(novoFuncionario);
			break;
		}
		case 2:
			// Calcular folha de pagamento
			emp.calcularFolhaPagto();
			break;
		case 3:
			// Exibir funções dos funcionários
			emp.exibirFuncoesFuncionarios();
			break;
		case 4:
			// Sair do programa
			std::cout << "Saindo do programa." << std::endl;
			break;
		case 5:
			emp.listarFuncionarios();
			break;
		case 6:
		{
			// Demitir funcionário por código
			std::string codigo;
			std::cout << "Digite o código do funcionário a demitir: ";
			std::cin >> codigo;
			emp.demitirFuncionario(codigo);
			break;
		}
		default:
			std::cout << "Escolha inválida. Tente novamente." << std::endl;
		}

		// Pausa o programa para que o usuário possa ver a saída
		std::cout << "Pressione Enter para continuar...";
		std::cin.ignore();
		std::cin.get();

	} while (escolha != 6);

	return 0;
}