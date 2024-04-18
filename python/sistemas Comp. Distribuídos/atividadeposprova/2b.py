import socket as sc
import threading as td

host = 'localhost'
port = 8888

def trata_msg(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print("[Cliente]:", data.decode())
        except Exception as e:
            print("Erro:", e)
            break
    client_socket.close()

server = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
server.bind((host, port))
server.listen(5)
print("[Servidor] Esperando conexões...")

while True:
    try:
        client_sock, addr = server.accept()
        print("[Servidor] Conexão estabelecida com:", addr)
        client_handler = td.Thread(target=trata_msg, args=(client_sock,))
        client_handler.start()
    except Exception as e:
        print("Erro:", e)
        break
    finally:
        server.close()
