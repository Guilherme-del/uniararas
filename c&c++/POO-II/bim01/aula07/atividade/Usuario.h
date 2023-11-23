#ifndef USUARIO_H
#define USUARIO_H

#include <string>
#include <vector>
#include "SocialNetwork.h"

class Usuario {
private:
    std::string nomeCompleto;
    std::string email;
    std::string dataCriacao;
    std::vector<SocialNetwork*> redesSociais;

public:
    Usuario(std::string nomeCompleto, std::string email);
    ~Usuario();

    // Funcionalidades
    void cadastrarNaRede(SocialNetwork* rede);
    void descadastrarDaRede(std::string nomeRede);
    SocialNetwork* pesquisarRedePorCodigo(int codigo);
    void visualizarRedesCadastradas() const;
    const std::vector<SocialNetwork*>& getRedesSociais() const;
};

#endif // USUARIO_H
