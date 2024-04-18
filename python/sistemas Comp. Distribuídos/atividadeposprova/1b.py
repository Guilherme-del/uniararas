import socket as sc

host = '127.0.0.50'
port = 8585

cliente = sc.socket(family=sc.AF_INET, type=sc.SOCK_DGRAM)

while True:
    mensagem = input("Digite a mensagem (ou 'sair' para sair): ")
    cliente.sendto(mensagem.encode(), (host, port))
    if mensagem.lower() == "sair":
        print("Conexão encerrada.")
        break
    resposta, _ = cliente.recvfrom(1024)
    print("Resposta do servidor:", resposta.decode())

cliente.close()
