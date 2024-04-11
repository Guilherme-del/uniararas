import requests

url = "https://raw.githubusercontent.com/marciliooliveira/atividade_sd/main/Atividade_MA1.pdf"
nome_do_arquivo = "Atividade_MA1.pdf"

# Faz a requisição GET
response = requests.get(url, stream=True)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Abre o arquivo para escrita em modo binário
    with open(nome_do_arquivo, "wb") as file:
        # Itera o conteúdo e escreve no arquivo
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
    print("Download completo.")
else:
    print("Falha ao baixar o arquivo.")
