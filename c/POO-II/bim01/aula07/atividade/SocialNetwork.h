#ifndef SOCIALNETWORK_H
#define SOCIALNETWORK_H

#include <string>
#include <vector>
#include "Post.h"

class SocialNetwork {
private:
    std::string nome;
    std::string dataCriacao;
    std::vector<Post*> posts;

public:
    SocialNetwork(std::string nome, std::string dataCriacao);

    // Getters
    std::string getNome() const;
    int getQuantidadePosts() const;
    const std::vector<Post*>& getPosts() const;

    // Funcionalidades
    Post* criarPost(std::string descricao,std::string tipo);
    void visualizarPosts() const;
};

#endif // SOCIALNETWORK_H
