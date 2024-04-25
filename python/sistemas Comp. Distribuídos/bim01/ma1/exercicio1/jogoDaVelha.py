import socket
import sys

# Define o tamanho do tabuleiro
BOARD_SIZE = 3
# Define o símbolo para cada jogador
SYMBOLS = ['X', 'O']

# Função para imprimir o tabuleiro
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * (4 * BOARD_SIZE - 1))

# Função para verificar se há um vencedor
def check_winner(board, symbol):
    # Verifica linhas e colunas
    for i in range(BOARD_SIZE):
        if all(board[i][j] == symbol for j in range(BOARD_SIZE)) or all(board[j][i] == symbol for j in range(BOARD_SIZE)):
            return True
    # Verifica diagonais
    if all(board[i][i] == symbol for i in range(BOARD_SIZE)) or all(board[i][BOARD_SIZE - 1 - i] == symbol for i in range(BOARD_SIZE)):
        return True
    return False

# Função para verificar se o tabuleiro está cheio
def check_draw(board):
    return all(board[i][j] != ' ' for i in range(BOARD_SIZE) for j in range(BOARD_SIZE))

# Função para processar a jogada do jogador
def process_move(board, row, col, symbol):
    if board[row][col] == ' ':
        board[row][col] = symbol
        return True
    return False

# Função principal do servidor
def main_server():
    # Cria o socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Define a porta e o endereço IP para o servidor
    server_address = ('localhost', 8888)
    # Faz o bind do socket com o endereço e a porta
    server_socket.bind(server_address)
    # Coloca o servidor no modo de escuta
    server_socket.listen(2)
    print("Aguardando conexões dos jogadores...")
    # Aceita as conexões dos jogadores
    player1_conn, player1_address = server_socket.accept()
    print("Jogador 1 conectado:", player1_address)
    player2_conn, player2_address = server_socket.accept()
    print("Jogador 2 conectado:", player2_address)
    # Inicializa o tabuleiro
    board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    # Loop principal do jogo

    current_player = 0
    while True:
        # Envia o estado atual do tabuleiro para ambos os jogadores
        for conn in [player1_conn, player2_conn]:
            conn.sendall(bytes("Estado atual do tabuleiro:\n", 'utf-8'))
            print_board(board)
            conn.sendall(bytes("\n", 'utf-8'))

        # Envia a vez do jogador atual
        player_symbol = SYMBOLS[current_player]
        player_conn = [player1_conn, player2_conn][current_player]
        player_conn.sendall(bytes("Sua vez de jogar (símbolo {}):\n".format(player_symbol), 'utf-8'))
        # Recebe a jogada do jogador
        move = player_conn.recv(1024).decode().strip().split(',')
        row, col = int(move[0]), int(move[1])
        # Processa a jogada
        if process_move(board, row, col, player_symbol):
            # Verifica se houve um vencedor ou empate
            if check_winner(board, player_symbol):
                player_conn.sendall(bytes("Parabéns! Você ganhou!\n", 'utf-8'))
                break
            elif check_draw(board):
                player_conn.sendall(bytes("O jogo empatou!\n", 'utf-8'))
                break
            # Alterna para o próximo jogador
            current_player = (current_player + 1) % 2
        else:
            player_conn.sendall(bytes("Jogada inválida. Tente novamente.\n", 'utf-8'))

    # Fecha as conexões
    player1_conn.close()
    player2_conn.close()
    server_socket.close()

# Função principal do cliente
def main_client():
    # Cria o socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Define o endereço e a porta do servidor
    server_address = ('localhost', 8888)
    # Conecta ao servidor
    client_socket.connect(server_address)

    while True:
        # Recebe e imprime o estado atual do tabuleiro
        server_response = ""
        while True:
            chunk = client_socket.recv(1024).decode()
            server_response += chunk
            if "\n" in chunk:
                break
        print(server_response, end='')  # End='' ensures no newline is added
        # Force flushing the output immediately
        sys.stdout.flush()
        # If the message indicates it's the player's turn
        if "Sua vez" in server_response:
            # Solicita a jogada ao jogador
            move = input("Digite a linha e a coluna da sua jogada (separadas por vírgula): ")
            client_socket.sendall(bytes(move, 'utf-8'))
        # If the message indicates the game result
        elif "ganhou" in server_response or "empatou" in server_response:
            print(server_response)
            break
    # Fecha a conexão
    client_socket.close()
# Função principal valida se o usuário digitou server ou client
if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "server":
        main_server()
    elif len(sys.argv) == 2 and sys.argv[1] == "client":
        main_client()
    else:
        print("Uso: python jogo_da_velha.py [server|client]")
