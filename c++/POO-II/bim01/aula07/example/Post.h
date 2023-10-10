#ifndef _post_h_
#define _post_h_

#include <string>
#include <iostream>

using namespace std;

class Post {

private:
    string descricao;
    int codigo;
    int likes;
public:
    Post(string descricao, int codigo);
    string getDescricao();
    void setDescricao(string descricao);
    int getCodigo();
    void setCodigo(int codigo);
    int getLikes();
    void curtir();
    virtual void compartilhar()=0;
};


#endif // !_post_h
