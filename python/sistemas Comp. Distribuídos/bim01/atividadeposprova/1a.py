import socket as sc

hosts = '127.0.0.50'
port = 8585

servidor = sc.socket(family=sc.AF_INET, type=sc.SOCK_DGRAM)
servidor.bind((hosts, port))

print("Aguardando conexão...")

while True:
    data, addr = servidor.recvfrom(1024)
    print("Cliente conectado:", addr)
    servidor.sendto(b"Conectado", addr)
    
    while True:
        mensagem = servidor.recvfrom(1024).decode()
        print("Mensagem recebida:", mensagem)
        if mensagem.lower() == "sair":
            print("Conexão encerrada pelo cliente.")
            break
        servidor.sendto(b"Ok", addr)
