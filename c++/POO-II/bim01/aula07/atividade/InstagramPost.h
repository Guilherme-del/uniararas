#ifndef INSTAGRAMPOST_H
#define INSTAGRAMPOST_H

#include "Post.h"

class InstagramPost : public Post {
public:
    InstagramPost(std::string descricao);
    void compartilhar() override;
};

#endif // INSTAGRAMPOST_H
