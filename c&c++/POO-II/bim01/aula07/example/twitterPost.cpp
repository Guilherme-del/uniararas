#include "twitterPost.h"
#include <iostream>
using namespace std;

TwitterPost::TwitterPost(int codigo, string& descricao) : Post(descricao,codigo) {}

void TwitterPost::compartilhar() {
    cout << "Post compartilhado no Twitter." << endl;
}
