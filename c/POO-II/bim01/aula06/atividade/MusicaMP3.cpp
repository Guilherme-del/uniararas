#include "MusicaMP3.h"
#include <iostream>

MusicaMP3::MusicaMP3(const std::string& titulo, const std::string& album, const std::string& compositor, const std::string& interprete, int ano, int tamanho)
    : Musica(titulo, album, compositor, interprete, ano), tamanhoEmBytes(tamanho) {}

void MusicaMP3::exibirInformacoes() const {
    Musica::exibirInformacoes();
    std::cout << "Tamanho (bytes): " << tamanhoEmBytes << std::endl;
}
