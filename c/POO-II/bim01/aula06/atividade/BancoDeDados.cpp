#include "BancoDeDados.h"
#include <iostream>

void BancoDeDados::adicionarMusica(Musica* musica) {
    musicas.push_back(musica);
}

void BancoDeDados::removerMusica(const std::string& titulo) {
    for (auto it = musicas.begin(); it != musicas.end(); ++it) {
        if ((*it)->getTitulo() == titulo) {
            delete *it;
            musicas.erase(it);
            std::cout << "Música removida: " << titulo << std::endl;
            return;
        }
    }
    std::cout << "Música não encontrada: " << titulo << std::endl;
}

void BancoDeDados::buscarPorAno(int ano) const {
    std::cout << "Músicas do ano " << ano << ":" << std::endl;
    for (const Musica* musica : musicas) {
        if (musica->getAno() == ano) {
            musica->exibirInformacoes();
            std::cout << std::endl;
        }
    }
}

void BancoDeDados::buscarPorCompositor(const std::string& compositor) const {
    std::cout << "Músicas do compositor " << compositor << ":" << std::endl;
    for (const Musica* musica : musicas) {
        if (musica->getCompositor() == compositor) {
            musica->exibirInformacoes();
            std::cout << std::endl;
        }
    }
}

void BancoDeDados::exibirTodasMusicas() const {
    std::cout << "Todas as músicas na biblioteca:" << std::endl;
    for (const Musica* musica : musicas) {
        musica->exibirInformacoes();
        std::cout << std::endl;
    }
}

std::vector<Musica*>& BancoDeDados::getMusicas() {
    return musicas;
}