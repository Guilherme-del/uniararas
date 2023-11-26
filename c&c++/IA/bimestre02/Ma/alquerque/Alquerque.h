#ifndef ALQUERQUE_H
#define ALQUERQUE_H

#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>

void imprimirTabuleiro(const std::vector<std::vector<char>>& tabuleiro);
bool movimentoValido(const std::vector<std::vector<char>>& tabuleiro, std::pair<int, int> inicio, std::pair<int, int> fim);
void aplicarMovimento(std::vector<std::vector<char>>& tabuleiro, std::pair<int, int> inicio, std::pair<int, int> fim);
std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>> obterMovimentosPossiveis(const std::vector<std::vector<char>>& tabuleiro, char jogador);
int heuristica(const std::vector<std::vector<char>>& tabuleiro);
int minimax(std::vector<std::vector<char>>& tabuleiro, int profundidade, bool maximizando_jogador);
std::pair<std::pair<int, int>, std::pair<int, int>> obterMelhorMovimento(std::vector<std::vector<char>>& tabuleiro, char jogador);
void jogarJogo();

#endif  // ALQUERQUE_H
