#include "usuario.h"

Usuario::Usuario(string nome) {
	this->nomeCompleto = nome;
	time_t agora;
	time(&agora);
	char buffer[26];
	ctime_s(buffer, sizeof(buffer), &agora);
	this->Data = buffer;
}

void Usuario::setNome(string nome) {
	this->nomeCompleto = nome;
}

string Usuario::getNome() {
	return this->nomeCompleto;
}

void Usuario::descadastrar(string nomeRede) {
	for (int i = 0; i < Redes.size(); i++) {
		if (this->Redes[i]->getNome() == nomeRede) {
			this->Redes.erase(this->Redes.begin() + i);
		}
	}
}
void Usuario::cadastrar(socialNetwork* social) {
	this->Redes.push_back(social);
}

socialNetwork* Usuario::getRede(string nomeRede) {
	for (int i = 0; i < this->Redes.size(); i++) {
		if (this->Redes[i]->getNome() == nomeRede) {
			return this->Redes[i];
		}
		
	}
	return NULL;
}

void Usuario::adicionaPost(string nomeRede, Post* post) {
	for (int i = 0; i < this->Redes.size(); i++) {
		if (this->Redes[i]->getNome() == nomeRede) {
			this->Redes[i]->postar(post);
		}
	}
}

void Usuario::curtirPost(string nomeRede, int codigo) {
	for (int i = 0; i < this->Redes.size(); i++) {
		if (this->Redes[i]->getNome() == nomeRede) {
			Redes[i]->curtirPost(codigo);
		}
	}
}
void Usuario::compPost(string nomeRede, int codigo) {
	for (int i = 0; i < this->Redes.size(); i++) {
		if (this->Redes[i]->getNome() == nomeRede) {
			Redes[i]->compPost(codigo);
		}
	}
}