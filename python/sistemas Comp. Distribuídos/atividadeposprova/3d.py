
import requests

base_url = 'http://localhost:5000'

# JSON de exemplo para enviar ao servidor
json_data = {
    "total": 200,
    "url": "htpp://api.engcomp2024.com",
    "dados": [
        {"relevante": "conteudo 1"},
        {"relevante": "conteudo 2"}
    ]
}

response = requests.post(f'{base_url}/receber_json', json=json_data)
print(response.json()) # Exibirá mensagem de sucesso ou erro

response = requests.get(f'{base_url}/todos_itens')
print(response.json())  # Exibirá todos os itens armazenados no servidor

response = requests.get(f'{base_url}/item/0')
print(response.json())  # Exibirá o item sob a chave "dados" na posição 0

response = requests.get(f'{base_url}/item/100')
print(response.json())  # Exibirá mensagem de erro