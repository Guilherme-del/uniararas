#include "MusicaCD.h"
#include <iostream>

MusicaCD::MusicaCD(const std::string& titulo, const std::string& album, const std::string& compositor, const std::string& interprete, int ano)
    : Musica(titulo, album, compositor, interprete, ano) {}

void MusicaCD::exibirInformacoes() const {
    Musica::exibirInformacoes();
}
