// TwitterPost.h
#ifndef TWITTERPOST_H
#define TWITTERPOST_H

#include "Post.h"

class TwitterPost : public Post {
public:
    TwitterPost(std::string descricao);
    void compartilhar() override;
};

#endif // TWITTERPOST_H
