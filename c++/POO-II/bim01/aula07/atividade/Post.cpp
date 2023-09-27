#include "Post.h"

int Post::proximoCodigo = 1;

Post::Post(std::string descricao)
    : codigo(proximoCodigo++), descricao(descricao), likes(0) {}

Post::~Post() {}

int Post::getCodigo() const {
    return codigo;
}

std::string Post::getDescricao() const {
    return descricao;
}

int Post::getLikes() const {
    return likes;
}

void Post::curtir() {
    likes++;
}
