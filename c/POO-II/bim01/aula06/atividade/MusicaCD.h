#ifndef MUSICACD_H
#define MUSICACD_H

#include "Musica.h"

class MusicaCD : public Musica {
public:
    MusicaCD(const std::string& titulo, const std::string& album, const std::string& compositor, const std::string& interprete, int ano);
    void exibirInformacoes() const override;
};

#endif // MUSICACD_H
