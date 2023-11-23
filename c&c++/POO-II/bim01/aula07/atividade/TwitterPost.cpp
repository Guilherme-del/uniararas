#include "TwitterPost.h"
#include <iostream>

TwitterPost::TwitterPost(std::string descricao)
    : Post(descricao) {}

void TwitterPost::compartilhar() {
    std::cout << "Compartilhando no Twitter: " << getDescricao() << std::endl;
}
