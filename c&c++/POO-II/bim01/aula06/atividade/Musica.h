#ifndef MUSICA_H
#define MUSICA_H

#include <string>

class Musica {
public:
    Musica(const std::string& titulo, const std::string& album, const std::string& compositor, const std::string& interprete, int ano);
    virtual ~Musica();
    
    virtual void exibirInformacoes() const;
    
    std::string getTitulo() const;
    std::string getCompositor() const;
    int getAno() const;

private:
    std::string titulo;
    std::string album;
    std::string compositor;
    std::string interprete;
    int ano;
};

#endif // MUSICA_H
