#ifndef _instagramPost_h
#define _instagramPost_h

#include "Post.h"

// Uso do polimorfismo aqui pois elas herdam da classe Post o compartilhar, porem implementam de forma diferente
class InstagramPost : public Post {
public:
    InstagramPost(int codigo, const  string& descricao);

    void compartilhar();
};

#endif
