#include "post.h"

Post::Post(string descricao, int codigo) {
    this->descricao = descricao;
    this->codigo = codigo;
    this->likes = 0;
}
void Post::curtir() {
    this->likes += 1;
}

void Post::setDescricao(string descricao) {
	this->descricao = descricao;
}

string Post::getDescricao() {
	return this->descricao;
}

void Post::setCodigo(int codigo) {
	this->codigo = codigo;
}

int Post::getCodigo() {
	return this->codigo;
}
int Post::getLikes() {
	return this->likes;
}
