#include "MusicaMP3.h"
#include "MusicaLP.h"
#include "MusicaCD.h"
#include "BancoDeDados.h"
#include <iostream>

int main() {
    BancoDeDados bancoDeDados;
    int opcao;

    do {
        std::cout << "\nMenu:\n";
        std::cout << "1. Adicionar música\n";
        std::cout << "2. Remover música\n";
        std::cout << "3. Buscar por ano\n";
        std::cout << "4. Buscar por compositor\n";
        std::cout << "5. Exibir todas as músicas\n";
        std::cout << "6. Encerrar programa\n";
        std::cout << "Escolha uma opção: ";
        std::cin >> opcao;

        switch (opcao) {
            case 1: {
                std::cout << "Escolha o tipo de música (1 - MP3, 2 - LP, 3 - CD): ";
                int tipo;
                std::cin >> tipo;

                std::string titulo, album, compositor, interprete;
                int ano;
                if (tipo == 1) {
                    int tamanho;
                    std::cout << "Título: ";
                    std::cin >> titulo;
                    std::cout << "Álbum: ";
                    std::cin >> album;
                    std::cout << "Compositor: ";
                    std::cin >> compositor;
                    std::cout << "Intérprete: ";
                    std::cin >> interprete;
                    std::cout << "Ano: ";
                    std::cin >> ano;
                    std::cout << "Tamanho (bytes): ";
                    std::cin >> tamanho;
                    bancoDeDados.adicionarMusica(new MusicaMP3(titulo, album, compositor, interprete, ano, tamanho));
                } else if (tipo == 2) {
                    int velocidade;
                    std::cout << "Título: ";
                    std::cin >> titulo;
                    std::cout << "Álbum: ";
                    std::cin >> album;
                    std::cout << "Compositor: ";
                    std::cin >> compositor;
                    std::cout << "Intérprete: ";
                    std::cin >> interprete;
                    std::cout << "Ano: ";
                    std::cin >> ano;
                    std::cout << "Velocidade (RPM): ";
                    std::cin >> velocidade;
                    bancoDeDados.adicionarMusica(new MusicaLP(titulo, album, compositor, interprete, ano, velocidade));
                } else if (tipo == 3) {
                    std::cout << "Título: ";
                    std::cin >> titulo;
                    std::cout << "Álbum: ";
                    std::cin >> album;
                    std::cout << "Compositor: ";
                    std::cin >> compositor;
                    std::cout << "Intérprete: ";
                    std::cin >> interprete;
                    std::cout << "Ano: ";
                    std::cin >> ano;
                    bancoDeDados.adicionarMusica(new MusicaCD(titulo, album, compositor, interprete, ano));
                } else {
                    std::cout << "Tipo inválido!\n";
                }
                break;
            }
            case 2: {
                std::string titulo;
                std::cout << "Digite o título da música a ser removida: ";
                std::cin >> titulo;
                bancoDeDados.removerMusica(titulo);
                break;
            }
            case 3: {
                int ano;
                std::cout << "Digite o ano a ser buscado: ";
                std::cin >> ano;
                bancoDeDados.buscarPorAno(ano);
                break;
            }
            case 4: {
                std::string compositor;
                std::cout << "Digite o compositor a ser buscado: ";
                std::cin >> compositor;
                bancoDeDados.buscarPorCompositor(compositor);
                break;
            }
            case 5: {
                bancoDeDados.exibirTodasMusicas();
                break;
            }
            case 6: {
                std::cout << "Encerrando o programa...\n";
                break;
            }
            default:
                std::cout << "Opção inválida!\n";
                break;
        }
    } while (opcao != 6);

    // Limpar memória alocada para as músicas
    for (Musica* musica : bancoDeDados.getMusicas()) {
        delete musica;
    }

    return 0;
}
