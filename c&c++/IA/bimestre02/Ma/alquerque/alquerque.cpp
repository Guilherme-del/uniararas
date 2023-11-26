#include "alquerque.h"

Game::Game() : tabuleiro{{'2', '2', '2', '2', '2'},
                     {'2', '2', '2', '2', '2'},
                     {'2', '2', '.', '1', '1'},
                     {'1', '1', '1', '1', '1'},
                     {'1', '1', '1', '1', '1'}} {}

void Game::exibirTabuleiro() const {
    std::cout << "  0 1 2 3 4\n";
    for (int i = 0; i < 5; ++i) {
        std::cout << i << " ";
        for (int j = 0; j < 5; ++j) {
            std::cout << tabuleiro[i][j] << " ";
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;
}

bool Game::movimentoValido(const std::pair<int, int>& inicio, const std::pair<int, int>& fim) const {
    if (tabuleiro[inicio.first][inicio.second] == '.') {
        return false;
    }
    if (tabuleiro[fim.first][fim.second] != '.') {
        return false;
    }
    return true;
}

void Game::aplicarMovimento(const std::pair<int, int>& inicio, const std::pair<int, int>& fim) {
    char jogador = tabuleiro[inicio.first][inicio.second];
    tabuleiro[inicio.first][inicio.second] = '.';
    tabuleiro[fim.first][fim.second] = jogador;
}

std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>> Game::obterMovimentosPossiveis(char jogador) const {
    std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>> movimentos;
    for (int i = 0; i < 5; ++i) {
        for (int j = 0; j < 5; ++j) {
            if (tabuleiro[i][j] == jogador) {
                for (int di : {-1, 0, 1}) {
                    for (int dj : {-1, 0, 1}) {
                        int ni = i + di, nj = j + dj;
                        if (0 <= ni && ni < 5 && 0 <= nj && nj < 5 && movimentoValido({i, j}, {ni, nj})) {
                            movimentos.push_back({{i, j}, {ni, nj}});
                        }

                        // Verificar movimentos de captura
                        int capture_i = i + 2 * di, capture_j = j + 2 * dj;
                        if (0 <= capture_i && capture_i < 5 && 0 <= capture_j && capture_j < 5 &&
                            tabuleiro[ni][nj] != jogador && movimentoValido({i, j}, {capture_i, capture_j})) {
                            movimentos.push_back({{i, j}, {capture_i, capture_j}});
                        }
                    }
                }
            }
        }
    }
    return movimentos;
}

int Game::heuristica() const {
    int contJogador1 = 0, contJogador2 = 0;
    for (const auto& linha : tabuleiro) {
        contJogador1 += std::count(linha.begin(), linha.end(), '1');
        contJogador2 += std::count(linha.begin(), linha.end(), '2');
    }
    return contJogador1 - contJogador2;
}

int Game::minimax(int profundidade, bool jogadorMaximizando) {
    if (profundidade == 0) {
        return heuristica();
    }

    char jogador = jogadorMaximizando ? '1' : '2';
    auto movimentosPossiveis = obterMovimentosPossiveis(jogador);

    if (jogadorMaximizando) {
        int maxAvaliacao = std::numeric_limits<int>::min();
        for (const auto& movimento : movimentosPossiveis) {
            auto novoTabuleiro = tabuleiro;
            aplicarMovimento(movimento.first, movimento.second);
            int avaliacao = minimax(profundidade - 1, false);
            maxAvaliacao = std::max(maxAvaliacao, avaliacao);
        }
        return maxAvaliacao;
    } else {
        int minAvaliacao = std::numeric_limits<int>::max();
        for (const auto& movimento : movimentosPossiveis) {
            auto novoTabuleiro = tabuleiro;
            aplicarMovimento(movimento.first, movimento.second);
            int avaliacao = minimax(profundidade - 1, true);
            minAvaliacao = std::min(minAvaliacao, avaliacao);
        }
        return minAvaliacao;
    }
}

std::pair<std::pair<int, int>, std::pair<int, int>> Game::obterMelhorMovimento(char jogador) {
    auto movimentosPossiveis = obterMovimentosPossiveis(jogador);
    if (movimentosPossiveis.empty()) {
        return {{-1, -1}, {-1, -1}}; // Sem movimentos válidos
    }

    std::pair<std::pair<int, int>, std::pair<int, int>> melhorMovimento = {{-1, -1}, {-1, -1}};
    int melhorAvaliacao = (jogador == '1') ? std::numeric_limits<int>::min() : std::numeric_limits<int>::max();

    for (const auto& movimento : movimentosPossiveis) {
        auto novoTabuleiro = tabuleiro;
        aplicarMovimento(movimento.first, movimento.second);
        int avaliacao = minimax(2, jogador == '1');

        if ((jogador == '1' && avaliacao > melhorAvaliacao) || (jogador == '2' && avaliacao < melhorAvaliacao)) {
            melhorAvaliacao = avaliacao;
            melhorMovimento = movimento;
        }
    }

    return melhorMovimento;
}

void Game::jogar() {
    exibirTabuleiro();

    while (true) {
        // Vez do jogador humano
        std::pair<int, int> inicio, fim;
        std::cout << "Digite a posição inicial (linha coluna) para o jogador 1: ";
        std::cin >> inicio.first >> inicio.second;
        std::cout << "Digite a posição final (linha coluna) para o jogador 1: ";
        std::cin >> fim.first >> fim.second;

        if (movimentoValido(inicio, fim)) {
            aplicarMovimento(inicio, fim);
            exibirTabuleiro();
        } else {
            std::cout << "Movimento inválido. Tente novamente." << std::endl;
            continue;
        }

        // Verificar vitória do jogador 1
        int avaliacaoJogador1 = heuristica();
        if (avaliacaoJogador1 > 0) {
            std::cout << "Jogador 1 (humano) venceu!" << std::endl;
            break;
        }

        // Vez do jogador IA
        auto melhorMovimento = obterMelhorMovimento('2');

        if (melhorMovimento.first.first != -1 && melhorMovimento.second.first != -1) {
            aplicarMovimento(melhorMovimento.first, melhorMovimento.second);
            std::cout << "Jogador 2 moveu de " << melhorMovimento.first.first << " " << melhorMovimento.first.second
                      << " para " << melhorMovimento.second.first << " " << melhorMovimento.second.second << std::endl;
            exibirTabuleiro();
        } else {
            std::cout << "Jogador 2 não tem movimentos válidos. O jogo acabou." << std::endl;
            break;  // Encerrar o jogo se a IA não tiver movimentos válidos
        }

        // Verificar vitória do jogador 2
        int avaliacaoJogador2 = heuristica();
        if (avaliacaoJogador2 < 0) {
            std::cout << "Jogador 2 (IA) venceu!" << std::endl;
            break;
        }
    }
}

int main() {
    Game jogo; // Criação de uma instância da classe Game
    jogo.jogar(); // Chamada do método jogar da instância jogo
    return 0;
};