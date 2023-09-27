#ifndef POST_H
#define POST_H

#include <string>

class Post {
private:
    static int proximoCodigo;
    int codigo;
    std::string descricao;
    int likes;

public:
    Post(std::string descricao);
    virtual ~Post();

    int getCodigo() const;
    std::string getDescricao() const;
    int getLikes() const;
    void curtir();
    virtual void compartilhar() = 0;
};

#endif // POST_H
