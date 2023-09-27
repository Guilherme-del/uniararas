#include "InstagramPost.h"
#include <iostream>

InstagramPost::InstagramPost(std::string descricao)
    : Post(descricao) {}

void InstagramPost::compartilhar() {
    std::cout << "Compartilhando no Instagram: " << getDescricao() << std::endl;
}
