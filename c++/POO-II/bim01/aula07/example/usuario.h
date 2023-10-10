#ifndef _usuario_h
#define _usuario_h
#include"socialNetwork.h"
#include <string>
#include <iostream>
#include <vector>
#include <ctime>
using namespace std;
class Usuario {
	private:
		string nomeCompleto;
		vector<socialNetwork*> Redes;
		char* Data;
	public:
		Usuario(string nome);
		string  getNome();
		void setNome(string nome);
		void cadastrar(socialNetwork * social);
		void descadastrar(string nomeRede);
		socialNetwork* getRede(string nomeRede);
		void adicionaPost(string nomeRede, Post* post);
		void curtirPost(string nomeRede, int codigoPost);
		void compPost(string nomeRede, int codigoPost);
};

#endif // !_usuario_h
