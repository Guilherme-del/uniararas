/*
* 2)  Modele uma classe Empresa que possui os seguintes atributos:
		Raz�o Social; 
		Lista de Funcion�rios - use vector para isso;
	
	J� a classe Funcion�rio deve possuir:
		Nome;
		Sobrenome;
		Cargo;
		Codigo;
		Salario;
										  
	A classe Funcion�rio ser� base para as classes Professor e T�cnico, e deve
	ser abstrata. As classes filhas devem implementar um m�todo chamado ExecutarFuncao, 
	sobreescrevendo o m�todos da classe pai - que � puro. 
	Al�m disso, elas devem atribuir os demais valores convenientes para a classe pai.
	
	Voc� deve criar os set/get para os atributos das classes e, para a classe Empresa,
	voc� dever� ter fun��es que permitam:
	
	1. Calcular a folha de pagamento dos funcion�rios, exibindo as informa��es principais
		deles e o valor total da folha;
	2. Listar os funcion�rios da empresa;
	3. Permitir contratar um novo funcion�rio;
	4. Permitir demitir um funcion�rio existente;
	5. Exibir as fun��es que s�o executadas pelos funcion�rios dessa empresa;
	
	Utilize dos artif�cios de ponteiros/refer�ncias e demais conceitos - heran�a e polimorfismo 
	- para tornar o programa modular e eficiente. Fa�a um menu para a aplica��o, baseado no que foi
	visto em aula.

*/


#include <iostream>
#include "funcionario.h"
#include "empresa.h"


int main()
{
	Empresa emp("FHO");

	Professor prof("Marcilio", "Oliveira", "Prof", "P8888", 20);
	Tecnico tec("Joao", "Silva", "Tec", "T9999", 10);

	emp.contratarFuncionario(prof);
	emp.contratarFuncionario(tec);

	emp.calcularFolhaPagto();
	emp.exibirFuncoesFuncionarios();

	return 0;

}