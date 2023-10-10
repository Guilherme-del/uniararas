#include <iostream>
#include <vector>
#include <string>
#include "Jogo.h"
#include "JogoComprado.h"
#include "JogoVendido.h"

int main()
{
    std::vector<Jogo *> colecao;
    int totalHorasJogadas = 0;
    int comprados = 0;
    std::string nome;
    std::string jogoNome;
    bool sair = false;

    while (!sair)
    {
        std::cout << "Menu:\n";
        std::cout << "1. Comprar jogo\n";
        std::cout << "2. Revender jogo\n";
        std::cout << "3. Exibir relatório da coleção\n";
        std::cout << "4. Exibir total de horas jogadas\n";
        std::cout << "5. Pesquisar jogo na coleção\n";
        std::cout << "6. Jogar um jogo\n";
        std::cout << "7. Sair\n";

        int opcao;
        std::cout << "Escolha uma opcao: " << std::endl;
        std::cin >> opcao;

        switch (opcao)
        {
        case 1:
        {
            bool encontrado = false;
            if (comprados < 7)
            {
                int faixaEtaria;
                std::cout << "Nome do jogo: ";
                std::cin >> nome;
                std::cout << "Faixa etária do jogo: ";
                std::cin >> faixaEtaria;
                Jogo *jogo = new JogoComprado(nome, faixaEtaria);
                colecao.push_back(jogo);
                comprados++;
                std::cout << "Jogo comprado com sucesso!" << std::endl;
            }
            else
            {
                std::cout << "Limite de 7 jogos comprados atingido!" << std::endl;
            }
            break;
        }

        case 2:
        {
            bool encontrado = false;
            if (!colecao.empty())
            {
                std::cout << "Nome do jogo a ser revendido: ";
                std::cin >> nome;
                for (int i = 0; i < colecao.size(); i++)
                {
                    if (colecao[i]->getNome() == nome)
                    {
                        Jogo *jogo = new JogoVendido(colecao[i]->getNome(), colecao[i]->getFaixaEtaria());
                        totalHorasJogadas -= colecao[i]->getHorasJogadas();
                        delete colecao[i];
                        colecao[i] = jogo;
                        colecao.erase(colecao.begin() + i);
                        comprados--;
                        std::cout << "Jogo revendido com sucesso!" << std::endl;
                        encontrado = true;
                        break;
                    }
                }
            }
            if (!encontrado)
            {
                std::cout << "Jogo não encontrado na coleção." << std::endl;
            }
            break;
        }

        case 3:
        {
            bool encontrado = false;
            std::cout << "Nome do jogo a pesquisar: ";
            std::cin >> nome;
            for (const auto &jogo : colecao)
            {
                if (jogo->getNome() == nome)
                {
                    jogo->exibirDetalhes();
                    encontrado = true;
                    break;
                }
            }
            if (!encontrado)
            {
                std::cout << "Jogo não encontrado na coleção." << std::endl;
            }
            break;
        }

        case 4:
            std::cout << "Total de horas jogadas: " << totalHorasJogadas << "h" << std::endl;
            break;

        case 5:
        {
            bool encontrado = false;
            std::cout << "Nome do jogo a pesquisar: ";
            std::cin >> nome;
            for (const auto &jogo : colecao)
            {
                if (jogo->getNome() == nome)
                {
                    jogo->exibirDetalhes();
                    encontrado = true;
                    break;
                }
            }
            if (!encontrado)
            {
                std::cout << "Jogo não encontrado na coleção." << std::endl;
            }
            break;
        }

        case 6:
        {
            bool encontrado = false;
            int horasJogadas;
            std::cout << "Nome do jogo a jogar: ";
            std::cin >> jogoNome;
            std::cout << "Horas jogadas: ";
            std::cin >> horasJogadas;
            for (const auto &jogo : colecao)
            {
                if (jogo->getNome() == jogoNome)
                {
                    jogo->jogar(horasJogadas);
                    totalHorasJogadas += horasJogadas;
                    std::cout << "Horas jogadas no jogo '" << jogo->getNome() << "' atualizadas com sucesso." << std::endl;
                    encontrado = true;
                    break;
                }
            }
            if (!encontrado)
            {
                std::cout << "Jogo não encontrado na coleção." << std::endl;
            }
            break;
        }

        case 7:
        {
            sair = true;
            break;
        }
        default:
            std::cout << "Opção inválida!" << std::endl;
            break;
        }
    }

    // Libera a memória que foi alocada
    for (auto jogo : colecao)
    {
        delete jogo;
    }

    return 0;
}
