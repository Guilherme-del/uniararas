#include "SocialNetwork.h"
#include "Post.h"
#include "TwitterPost.h"
#include "InstagramPost.h"
#include <iostream>

SocialNetwork::SocialNetwork(std::string nome, std::string dataCriacao)
    : nome(nome), dataCriacao(dataCriacao) {}

std::string SocialNetwork::getNome() const {
    return nome;
}

int SocialNetwork::getQuantidadePosts() const {
    return posts.size();
}

const std::vector<Post*>& SocialNetwork::getPosts() const { // Add this implementation
    return posts;
}

Post* SocialNetwork::criarPost(std::string descricao, std::string tipo) {
    Post* novoPost = nullptr;

    if (tipo == "Twitter") {
        novoPost = new TwitterPost(descricao);
    } else if (tipo == "Instagram") {
        novoPost = new InstagramPost(descricao);
    } else {
        std::cout << "Tipo de rede social inválido." << std::endl;
    }

    if (novoPost) {
        posts.push_back(novoPost);
    }

    return novoPost;
}


void SocialNetwork::visualizarPosts() const {
    std::cout << "Posts na rede " << nome << ":" << std::endl;
    for (const auto& post : posts) {
        std::cout << "Descrição: " << post->getDescricao() << " Likes: " << post->getLikes() << std::endl;
    }
}
