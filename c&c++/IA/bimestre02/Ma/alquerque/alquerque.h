// game.h
#ifndef alquerque_H
#define alquerque_H

#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>

class Game {
public:
    Game();
    void jogar();

private:
    void exibirTabuleiro() const;
    bool movimentoValido(const std::pair<int, int>& inicio, const std::pair<int, int>& fim) const;
    void aplicarMovimento(const std::pair<int, int>& inicio, const std::pair<int, int>& fim);
    std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>> obterMovimentosPossiveis(char jogador) const;
    int heuristica() const;
    int minimax(int profundidade, bool jogadorMaximizando);
    std::pair<std::pair<int, int>, std::pair<int, int>> obterMelhorMovimento(char jogador);

    std::vector<std::vector<char>> tabuleiro;
};

#endif // alquerque_H
