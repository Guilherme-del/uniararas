#ifndef _twitterPost_h_
#define _twitterPost_h_
#include"Post.h"
#include <string>
#include <iostream>
using namespace std;

// Uso do polimorfismo aqui pois elas herdam da classe Post o compartilhar, porem implementam de forma diferente
class TwitterPost : public Post {
public:
    TwitterPost(int codigo, string& descricao);

    void compartilhar();
};

#endif