#ifndef MUSICAMP3_H
#define MUSICAMP3_H

#include "Musica.h"

class MusicaMP3 : public Musica {
public:
    MusicaMP3(const std::string& titulo, const std::string& album, const std::string& compositor, const std::string& interprete, int ano, int tamanho);
    void exibirInformacoes() const override;
    
private:
    int tamanhoEmBytes;
};

#endif // MUSICAMP3_H