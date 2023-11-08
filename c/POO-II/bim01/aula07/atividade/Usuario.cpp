#include "Usuario.h"
#include <iostream>
#include <ctime>

Usuario::Usuario(std::string nomeCompleto, std::string email)
    : nomeCompleto(nomeCompleto), email(email) {
    // Obtém a data atual
    std::time_t currentTime = std::time(nullptr);
    dataCriacao = std::ctime(&currentTime);
}

Usuario::~Usuario() {
    // Limpa a memória dos objetos SocialNetwork criados
    for (auto& rede : redesSociais) {
        delete rede;
    }
}

void Usuario::cadastrarNaRede(SocialNetwork* rede) {
    redesSociais.push_back(rede);
}

void Usuario::descadastrarDaRede(std::string nomeRede) {
    for (auto it = redesSociais.begin(); it != redesSociais.end(); ++it) {
        if ((*it)->getNome() == nomeRede) {
            redesSociais.erase(it);
            break;
        }
    }
}

SocialNetwork* Usuario::pesquisarRedePorCodigo(int codigo) {
    for (auto& rede : redesSociais) {
        if (rede->getQuantidadePosts() > 0) {
            return rede;
        }
    }
    return nullptr;
}

void Usuario::visualizarRedesCadastradas() const {
    std::cout << "Redes cadastradas para o usuário " << nomeCompleto << ":" << std::endl;
    for (const auto& rede : redesSociais) {
        std::cout << "- " << rede->getNome() << std::endl;
    }
}

const std::vector<SocialNetwork*>& Usuario::getRedesSociais() const {
    return redesSociais;
}