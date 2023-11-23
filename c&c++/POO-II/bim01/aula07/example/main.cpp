
#include <iostream>
#include "usuario.h"
#include "socialNetwork.h"
#include "post.h"
#include "twitterPost.h"
#include "instagramPost.h"
#include <ctime>

using namespace std;

void menu(int &op) {
	cout << "[1] Cadastrar rede social:" << endl;
	cout << "[2] Descadastrar rede social:" << endl;
	cout << "[3] Usar rede social:" << endl;
	cout << "[6] Sair" << endl;
	cin >> op;
}

void menuRede(int& op3) {
	cout << "[1] Criar post" << endl;
	cout << "[2] curtir " << endl;
	cout << "[3] compartilhar " << endl;
	cout << "[4] sair " << endl;	
	cin >> op3;
}

int main() {
	Usuario* u = new Usuario("Iago");
	int op, op2,op3;
	string redeSocial, descricao;
	int codigo;
	bool flag = true;
	string rede = "";

	Post* p;
	socialNetwork* s;
	while (true) {
		menu(op);

		switch (op) {
		case 1:
			// cout << "Digite o nome da rede social: " << endl;
			// cin >> redeSocial;
			cout << "[1] Twitter" << endl;
			cout << "[2] Instagram" << endl;
			cin >> op2;
			switch (op2) {
			case 1:
					redeSocial = "Twitter";
					s = new socialNetwork(redeSocial);
					u->cadastrar(s);
					break;
			case 2:
					redeSocial = "Instagram";
					s = new socialNetwork(redeSocial);
					u->cadastrar(s);
					break;
			}
			break;
		case 2:
			cout << "Digite o nome da rede social para descadastrar: " << endl;
			cin >> redeSocial;
			u->descadastrar(redeSocial);
			break;
		case 3:
				cout << "Digite qual rede deseja entrar: " << endl;
				cout << "[1] Twitter" << endl;
				cout << "[2] Instagram" << endl;
				cin >> op2;
				if (op2 == 1) {
					rede = "Twitter";
					flag = true;
				}
				else {
					flag = true;
					rede = "Instagram";
				}
				while (flag) {
				menuRede(op3);
				switch (op3) {
				case 1:
					switch (op2) {
					case 1:
						cout << "Digite a descricao do post: " << endl;
						cin >> descricao;
						cout << "Digite o codigo do post: " << endl;
						cin >> codigo;
						p = new TwitterPost(codigo, descricao);
						u->adicionaPost("Twitter", p);
						break;
					case 2:
						cout << "Digite a descricao do post: " << endl;
						cin >> descricao;
						cout << "Digite o codigo do post: " << endl;
						cin >> codigo;
						p = new InstagramPost(codigo, descricao);
						u->adicionaPost("Instagram", p);
						break;
					}
					break;
				case 2:
					cout << "Digite o codigo do post: " << endl;
					cin >> codigo;
					u->curtirPost(rede, codigo);
					break;
				case 3:
					cout<< "Digite o codigo do post: " << endl;
					cin >> codigo;
					u->compPost(rede, codigo);
					break;
				case 4:
					flag = false;
					break;
				}
			}
			break;
		
		case 5:
		case 6:
			return 0;
			break;
		default:
			cout << "Opcao invalida!" << endl;
		}
	}

	return 0;
}