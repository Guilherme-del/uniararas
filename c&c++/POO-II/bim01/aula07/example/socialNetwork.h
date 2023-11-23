#ifndef _socialNetwork_h
#define _socialNetwork_h
#include"Post.h"	
#include <string>
#include <iostream>
#include <vector>
using namespace std;
class socialNetwork {
private:
	string Nome;
	char* Data;
	vector<Post*> Posts;
public:
	void curtirPost(int cod);
	void compPost(int cod);
	socialNetwork(string nome);
	string getNome();
	void setNome(string nome);
	void postar(Post* post);
	void deletarPost(int cod);
};

#endif // !_socialNetwork_h
