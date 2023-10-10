#include "instagramPost.h"

InstagramPost::InstagramPost(int codigo, const  string& descricao) : Post(descricao, codigo) {}

void InstagramPost::compartilhar() {
    cout << "Post compartilhado no Instagram." << endl;
}
