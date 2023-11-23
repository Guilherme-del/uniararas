#include <iostream>
#include "Usuario.h"
#include "SocialNetwork.h"
#include "TwitterPost.h"
#include "InstagramPost.h"

int main() {
    std::string nome, email;
    std::cout << "Informe o nome completo do usuário: ";
    std::getline(std::cin, nome);
    std::cout << "Informe o email do usuário: ";
    std::getline(std::cin, email);

    Usuario usuario(nome, email);

    while (true) {
        std::cout << "\nOpções:" << std::endl;
        std::cout << "1. Cadastrar em uma rede social" << std::endl;
        std::cout << "2. Descadastrar de uma rede social" << std::endl;
        std::cout << "3. Criar um post" << std::endl;
        std::cout << "4. Curtir um post" << std::endl;
        std::cout << "5. Visualizar redes cadastradas" << std::endl;
        std::cout << "6. Sair" << std::endl;
        std::cout << "Escolha uma opção: ";

        int escolha;
        std::cin >> escolha;
        std::cin.ignore(); // Limpa o buffer do teclado

        switch (escolha) {
            case 1: {
                std::string nomeRede, dataCriacaoRede;
                std::cout << "Informe o nome da rede social: ";
                std::getline(std::cin, nomeRede);
                std::cout << "Informe a data de criação da rede social: ";
                std::getline(std::cin, dataCriacaoRede);
                SocialNetwork* rede = new SocialNetwork(nomeRede, dataCriacaoRede);
                usuario.cadastrarNaRede(rede);
                break;
            }
            case 2: {
                std::string nomeRede;
                std::cout << "Informe o nome da rede social a ser descadastrada: ";
                std::getline(std::cin, nomeRede);
                usuario.descadastrarDaRede(nomeRede);
                break;
            }
            case 3: {
                std::string descricao;
                std::string tipo;
                std::cout << "Informe a descrição do post: ";
                std::getline(std::cin, descricao);
                std::cout << "Informe em qual rede: ";
                std::getline(std::cin, tipo);
                SocialNetwork* rede = usuario.pesquisarRedePorCodigo(1); // Suponha que estamos usando a primeira rede
                if (rede != nullptr) {
                    Post* post = rede->criarPost(descricao,tipo);
                    std::cout << "Post criado com sucesso! Código: " << post->getCodigo() << std::endl;
                } else {
                    std::cout << "O usuário não está cadastrado em nenhuma rede social." << std::endl;
                }
                break;
            }
            case 4: {
                int codigo;
                std::cout << "Informe o código do post a ser curtido: ";
                std::cin >> codigo;
                SocialNetwork* rede = usuario.pesquisarRedePorCodigo(codigo);
                if (rede != nullptr) {
                    for (auto& post : rede->getPosts()) {
                        if (post->getCodigo() == codigo) {
                            post->curtir();
                            std::cout << "Post curtido com sucesso!" << std::endl;
                            break;
                        }
                    }
                } else {
                    std::cout << "O usuário não está cadastrado em nenhuma rede social." << std::endl;
                }
                break;
            }
            case 5: {
                usuario.visualizarRedesCadastradas();
                break;
            }
            case 6: {
                // Liberar a memória alocada
                for (auto& rede : usuario.getRedesSociais()) {
                    delete rede;
                }
                return 0;
            }
            default:
                std::cout << "Opção inválida. Tente novamente." << std::endl;
                break;
        }
    }

    return 0;
}
