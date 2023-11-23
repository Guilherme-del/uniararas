#ifndef MUSICALP_H
#define MUSICALP_H

#include "Musica.h"

class MusicaLP : public Musica {
public:
    MusicaLP(const std::string& titulo, const std::string& album, const std::string& compositor, const std::string& interprete, int ano, int velocidade);
    void exibirInformacoes() const override;
    
private:
    int velocidadeRPM;
};

#endif // MUSICALP_H
