#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

void print_board(const vector<vector<char>>& board) {
    for (const auto& row : board) {
        for (char cell : row) {
            cout << cell << " ";
        }
        cout << endl;
    }
    cout << endl;
}

bool is_valid_move(const vector<vector<char>>& board, pair<int, int> start, pair<int, int> end) {
    if (board[start.first][start.second] == '.') {
        return false;
    }
    if (board[end.first][end.second] != '.') {
        return false;
    }
    return true;
}

void apply_move(vector<vector<char>>& board, pair<int, int> start, pair<int, int> end) {
    char player = board[start.first][start.second];
    board[start.first][start.second] = '.';
    board[end.first][end.second] = player;
}

vector<pair<pair<int, int>, pair<int, int>>> get_possible_moves(const vector<vector<char>>& board, char player) {
    vector<pair<pair<int, int>, pair<int, int>>> moves;
    for (int i = 0; i < 5; ++i) {
        for (int j = 0; j < 5; ++j) {
            if (board[i][j] == player) {
                for (int di : {-1, 0, 1}) {
                    for (int dj : {-1, 0, 1}) {
                        int ni = i + di, nj = j + dj;
                        if (0 <= ni && ni < 5 && 0 <= nj && nj < 5 && is_valid_move(board, {i, j}, {ni, nj})) {
                            moves.push_back({{i, j}, {ni, nj}});
                        }

                        // Check for capturing moves
                        int capture_i = i + 2 * di, capture_j = j + 2 * dj;
                        if (0 <= capture_i && capture_i < 5 && 0 <= capture_j && capture_j < 5 &&
                            board[ni][nj] != player && is_valid_move(board, {i, j}, {capture_i, capture_j})) {
                            moves.push_back({{i, j}, {capture_i, capture_j}});
                        }
                    }
                }
            }
        }
    }
    return moves;
}

int evaluate(const vector<vector<char>>& board) {
    int count_player1 = 0, count_player2 = 0;
    for (const auto& row : board) {
        count_player1 += count(row.begin(), row.end(), '1');
        count_player2 += count(row.begin(), row.end(), '2');
    }
    return count_player1 - count_player2;
}

int minimax(vector<vector<char>>& board, int depth, bool maximizing_player) {
    if (depth == 0) {
        return evaluate(board);
    }

    char player = maximizing_player ? '1' : '2';
    auto possible_moves = get_possible_moves(board, player);

    if (maximizing_player) {
        int max_eval = numeric_limits<int>::min();
        for (const auto& move : possible_moves) {
            auto new_board = board;
            apply_move(new_board, move.first, move.second);
            int eval = minimax(new_board, depth - 1, false);
            max_eval = max(max_eval, eval);
        }
        return max_eval;
    } else {
        int min_eval = numeric_limits<int>::max();
        for (const auto& move : possible_moves) {
            auto new_board = board;
            apply_move(new_board, move.first, move.second);
            int eval = minimax(new_board, depth - 1, true);
            min_eval = min(min_eval, eval);
        }
        return min_eval;
    }
}


pair<pair<int, int>, pair<int, int>> get_best_move(vector<vector<char>>& board, char player) {
    auto possible_moves = get_possible_moves(board, player);
    if (possible_moves.empty()) {
        return {{-1, -1}, {-1, -1}}; // No valid moves
    }

    pair<pair<int, int>, pair<int, int>> best_move = {{-1, -1}, {-1, -1}};
    int best_eval = (player == '1') ? numeric_limits<int>::min() : numeric_limits<int>::max();

    for (const auto& move : possible_moves) {
        auto new_board = board;
        apply_move(new_board, move.first, move.second);
        int eval = minimax(new_board, 2, player == '1');

        if ((player == '1' && eval > best_eval) || (player == '2' && eval < best_eval)) {
            best_eval = eval;
            best_move = move;
        }
    }

    return best_move;
}


void play_game() {
    vector<vector<char>> board = {
        {'2', '2', '2', '2', '2'},
        {'2', '2', '2', '2', '2'},
        {'2', '2', '.', '1', '1'},
        {'1', '1', '1', '1', '1'},
        {'1', '1', '1', '1', '1'}
    };

    print_board(board);

    while (true) {
        // Vez do jogador 1 (humano)
        pair<int, int> start, end;
        cout << "Digite a posição inicial (linha coluna) para jogador 1: ";
        cin >> start.first >> start.second;
        cout << "Digite a posição final (linha coluna) para jogador 1: ";
        cin >> end.first >> end.second;

        cout << "Start: " << start.first << " " << start.second << endl;
        cout << "End: " << end.first << " " << end.second << endl;
        cout << "Is Valid Move: " << is_valid_move(board, start, end) << endl;

        if (is_valid_move(board, start, end)) {
            apply_move(board, start, end);
            print_board(board);
        } else {
            cout << "Movimento inválido. Tente novamente." << endl;
            continue;
        }

        // Vez do jogador 2 (IA)
        auto best_move = get_best_move(board, '2');

        if (best_move.first.first != -1 && best_move.second.first != -1) {
            apply_move(board, best_move.first, best_move.second);
            cout << "Jogador 2 moveu de " << best_move.first.first << " " << best_move.first.second
                 << " para " << best_move.second.first << " " << best_move.second.second << endl;
            print_board(board);
        } else {
            cout << "Jogador 2 não tem movimentos válidos. O jogo acabou." << endl;
            break;  // End the game if the AI has no valid moves
        }
    }
}

int main() {
    play_game();
    return 0;
}
