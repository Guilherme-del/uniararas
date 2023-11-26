#include "Alquerque.h"

using namespace std;

void imprimirTabuleiro(const vector<vector<char>>& tabuleiro) {
    cout << "   0  1  2  3  4" << endl;
    for (int i = 0; i < 5; ++i) {
        cout << i << " ";
        for (int j = 0; j < 5; ++j) {
            cout << "[" << tabuleiro[i][j] << "]";
        }
        cout << endl;
    }
    cout << endl;
}

bool movimentoValido(const vector<vector<char>>& tabuleiro, pair<int, int> inicio, pair<int, int> fim) {
    if (tabuleiro[inicio.first][inicio.second] == '.') {
        return false;
    }
    if (tabuleiro[fim.first][fim.second] != '.') {
        return false;
    }
    return true;
}

void aplicarMovimento(vector<vector<char>>& tabuleiro, pair<int, int> inicio, pair<int, int> fim) {
    char jogador = tabuleiro[inicio.first][inicio.second];
    tabuleiro[inicio.first][inicio.second] = '.';
    tabuleiro[fim.first][fim.second] = jogador;
}

vector<pair<pair<int, int>, pair<int, int>>> obterMovimentosPossiveis(const vector<vector<char>>& tabuleiro, char jogador) {
    vector<pair<pair<int, int>, pair<int, int>>> movimentos;
    for (int i = 0; i < 5; ++i) {
        for (int j = 0; j < 5; ++j) {
            if (tabuleiro[i][j] == jogador) {
                for (int di : {-1, 0, 1}) {
                    for (int dj : {-1, 0, 1}) {
                        int ni = i + di, nj = j + dj;
                        if (0 <= ni && ni < 5 && 0 <= nj && nj < 5 && movimentoValido(tabuleiro, {i, j}, {ni, nj})) {
                            movimentos.push_back({{i, j}, {ni, nj}});
                        }

                        // Verificar movimentos de captura
                        int captura_i = i + 2 * di, captura_j = j + 2 * dj;
                        if (0 <= captura_i && captura_i < 5 && 0 <= captura_j && captura_j < 5 &&
                            tabuleiro[ni][nj] != jogador && movimentoValido(tabuleiro, {i, j}, {captura_i, captura_j})) {
                            movimentos.push_back({{i, j}, {captura_i, captura_j}});
                        }
                    }
                }
            }
        }
    }
    return movimentos;
}

int heuristica(const vector<vector<char>>& tabuleiro) {
    int contagem_jogador1 = 0, contagem_jogador2 = 0;
    for (const auto& linha : tabuleiro) {
        contagem_jogador1 += count(linha.begin(), linha.end(), '1');
        contagem_jogador2 += count(linha.begin(), linha.end(), '2');
    }
    return contagem_jogador1 - contagem_jogador2;
}

int minimax(vector<vector<char>>& tabuleiro, int profundidade, bool maximizando_jogador) {
    if (profundidade == 0) {
        return heuristica(tabuleiro);
    }

    char jogador = maximizando_jogador ? '1' : '2';
    auto movimentos_possiveis = obterMovimentosPossiveis(tabuleiro, jogador);

    if (maximizando_jogador) {
        int max_aval = numeric_limits<int>::min();
        for (const auto& movimento : movimentos_possiveis) {
            auto novo_tabuleiro = tabuleiro;
            aplicarMovimento(novo_tabuleiro, movimento.first, movimento.second);
            int aval = minimax(novo_tabuleiro, profundidade - 1, false);
            max_aval = max(max_aval, aval);
        }
        return max_aval;
    } else {
        int min_aval = numeric_limits<int>::max();
        for (const auto& movimento : movimentos_possiveis) {
            auto novo_tabuleiro = tabuleiro;
            aplicarMovimento(novo_tabuleiro, movimento.first, movimento.second);
            int aval = minimax(novo_tabuleiro, profundidade - 1, true);
            min_aval = min(min_aval, aval);
        }
        return min_aval;
    }
}

pair<pair<int, int>, pair<int, int>> obterMelhorMovimento(vector<vector<char>>& tabuleiro, char jogador) {
    auto movimentos_possiveis = obterMovimentosPossiveis(tabuleiro, jogador);
    if (movimentos_possiveis.empty()) {
        return {{-1, -1}, {-1, -1}}; // Sem movimentos válidos
    }

    pair<pair<int, int>, pair<int, int>> melhor_movimento = {{-1, -1}, {-1, -1}};
    int melhor_aval = (jogador == '1') ? numeric_limits<int>::min() : numeric_limits<int>::max();

    for (const auto& movimento : movimentos_possiveis) {
        auto novo_tabuleiro = tabuleiro;
        aplicarMovimento(novo_tabuleiro, movimento.first, movimento.second);
        int aval = minimax(novo_tabuleiro, 2, jogador == '1');

        if ((jogador == '1' && aval > melhor_aval) || (jogador == '2' && aval < melhor_aval)) {
            melhor_aval = aval;
            melhor_movimento = movimento;
        }
    }

    return melhor_movimento;
}

void jogarJogo() {
    vector<vector<char>> tabuleiro = {
        {'2', '2', '2', '2', '2'},
        {'2', '2', '2', '2', '2'},
        {'2', '2', '.', '1', '1'},
        {'1', '1', '1', '1', '1'},
        {'1', '1', '1', '1', '1'}
    };

    imprimirTabuleiro(tabuleiro);

    while (true) {
        // Vez do jogador 1 (humano)
        pair<int, int> inicio, fim;
        cout << "Digite a posição inicial (linha coluna) para jogador 1: ";
        cin >> inicio.first >> inicio.second;
        cout << "Digite a posição final (linha coluna) para jogador 1: ";
        cin >> fim.first >> fim.second;

        cout << "Inicio: " << inicio.first << " " << inicio.second << endl;
        cout << "Fim: " << fim.first << " " << fim.second << endl;
        cout << "É um Movimento Válido: " << movimentoValido(tabuleiro, inicio, fim) << endl;

        if (movimentoValido(tabuleiro, inicio, fim)) {
            aplicarMovimento(tabuleiro, inicio, fim);
            imprimirTabuleiro(tabuleiro);
        } else {
            cout << "Movimento inválido. Tente novamente." << endl;
            continue;
        }

        // Vez do jogador 2 (IA)
        auto melhor_movimento = obterMelhorMovimento(tabuleiro, '2');

        if (melhor_movimento.first.first != -1 && melhor_movimento.second.first != -1) {
            aplicarMovimento(tabuleiro, melhor_movimento.first, melhor_movimento.second);
            cout << "Jogador 2 moveu de " << melhor_movimento.first.first << " " << melhor_movimento.first.second
                 << " para " << melhor_movimento.second.first << " " << melhor_movimento.second.second << endl;
            imprimirTabuleiro(tabuleiro);
        } else {
            cout << "Jogador 2 não tem movimentos válidos. O jogo acabou." << endl;
            break;  // Finalizar o jogo se a IA não tiver movimentos válidos
        }
    }

    // Copiar o estado final do tabuleiro
    vector<vector<char>> tabuleiro_final = tabuleiro;

    int resultado = heuristica(tabuleiro_final);

    if (resultado > 0) {
        cout << "Jogador 1 venceu!" << endl;
    } else if (resultado < 0) {
        cout << "Jogador 2 venceu!" << endl;
    } else {
        cout << "É um empate!" << endl;
    }
}