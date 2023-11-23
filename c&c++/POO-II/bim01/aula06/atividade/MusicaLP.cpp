#include "MusicaLP.h"
#include <iostream>

MusicaLP::MusicaLP(const std::string& titulo, const std::string& album, const std::string& compositor, const std::string& interprete, int ano, int velocidade)
    : Musica(titulo, album, compositor, interprete, ano), velocidadeRPM(velocidade) {}

void MusicaLP::exibirInformacoes() const {
    Musica::exibirInformacoes();
    std::cout << "Velocidade (RPM): " << velocidadeRPM << std::endl;
}
