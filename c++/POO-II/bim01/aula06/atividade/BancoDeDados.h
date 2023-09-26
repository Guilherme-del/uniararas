#ifndef BANCODEDADOS_H
#define BANCODEDADOS_H

#include "Musica.h"
#include <vector>
#include <string>

class BancoDeDados {
public:
    void adicionarMusica(Musica* musica);
    void removerMusica(const std::string& titulo);
    void buscarPorAno(int ano) const;
    void buscarPorCompositor(const std::string& compositor) const;
    void exibirTodasMusicas() const;
    std::vector<Musica*>& getMusicas();
    
private:
    std::vector<Musica*> musicas;
};

#endif // BANCODEDADOS_H