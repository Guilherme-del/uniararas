#include "Musica.h"
#include <iostream>

Musica::Musica(const std::string& titulo, const std::string& album, const std::string& compositor, const std::string& interprete, int ano)
    : titulo(titulo), album(album), compositor(compositor), interprete(interprete), ano(ano) {}

Musica::~Musica() {}

void Musica::exibirInformacoes() const {
    std::cout << "Título: " << titulo << std::endl;
    std::cout << "Álbum: " << album << std::endl;
    std::cout << "Compositor: " << compositor << std::endl;
    std::cout << "Intérprete: " << interprete << std::endl;
    std::cout << "Ano: " << ano << std::endl;
}

std::string Musica::getTitulo() const {
    return titulo;
}

std::string Musica::getCompositor() const {
    return compositor;
}

int Musica::getAno() const {
    return ano;
}