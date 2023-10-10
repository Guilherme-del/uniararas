#include "socialNetwork.h"

socialNetwork::socialNetwork(string nome) {

	this->Nome = nome;

	time_t agora;
	time(&agora);
	char buffer[26];
	ctime_s(buffer, sizeof(buffer), &agora);
	this->Data = buffer;
}

void socialNetwork::setNome(string nome) {
	this->Nome = nome;
}

string socialNetwork::getNome() {
	return this->Nome;
}

void socialNetwork::deletarPost(int cod) {
	for (int i = 0; i < Posts.size();i++) {
		if (this->Posts[i]->getCodigo() == cod) {
			this->Posts.erase(this->Posts.begin() + i);
		}
	}

}

void socialNetwork::postar(Post* post) {
	this->Posts.push_back(post);
}
void socialNetwork::curtirPost(int cod) {
	for (int i = 0; i < Posts.size(); i++) {
		if (this->Posts[i]->getCodigo() == cod) {
		 this->Posts[i]->curtir();
		}
	}
}
void socialNetwork::compPost(int cod) {
	for (int i = 0; i < Posts.size(); i++) {
		if (this->Posts[i]->getCodigo() == cod) {
			this->Posts[i]->compartilhar();
		}
	}
}