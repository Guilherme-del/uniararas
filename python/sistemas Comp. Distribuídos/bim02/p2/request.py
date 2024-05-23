import requests

# URL base da sua API Flask
base_url = "http://localhost:5000"  # Certifique-se de usar o endereço e porta corretos

# Função para fazer uma requisição GET para uma rota específica
def get_route(route):
    url = f"{base_url}/{route}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Erro ao acessar a rota {route}: {response.text}"

# Função para fazer uma requisição POST para uma rota específica
def post_route(route, data):
    url = f"{base_url}/{route}"
    response = requests.post(url, json=data)
    if response.status_code == 201:
        return response.json()
    else:
        return f"Erro ao acessar a rota {route}: {response.text}"

# Função para fazer uma requisição PUT para uma rota específica
def put_route(route, id, data):
    url = f"{base_url}/{route}/{id}"
    response = requests.put(url, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Erro ao acessar a rota {route}: {response.text}"

# Função para fazer uma requisição DELETE para uma rota específica
def delete_route(route, id):
    url = f"{base_url}/{route}/{id}"
    response = requests.delete(url)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Erro ao acessar a rota {route}: {response.text}"

# Exemplo de uso:
# Consumindo a rota para criar uma nova máquina
new_maquina_data = {
    "codigo": "MAQ001",
    "descricao": "Máquina de teste",
    "tipo": "Tipo A"
}
response = post_route("maquinas", new_maquina_data)
print("Rota POST /maquinas:", response)

# Consumindo a rota para obter todas as máquinas
maquinas = get_route("maquinas")
print("Rota GET /maquinas:", maquinas)

# Consumindo a rota para atualizar uma máquina específica
maquina_id = 1  # ID da máquina a ser atualizada
update_maquina_data = {
    "codigo": "MAQ002",
    "descricao": "Máquina de teste atualizada",
    "tipo": "Tipo B"
}
response = put_route("maquinas", maquina_id, update_maquina_data)
print(f"Rota PUT /maquinas/{maquina_id}:", response)

# Consumindo a rota para deletar uma máquina específica
response = delete_route("maquinas", maquina_id)
print(f"Rota DELETE /maquinas/{maquina_id}:", response)

# Consumindo a rota para criar uma nova manutenção
new_manutencao_data = {
    "descricao": "Manutenção de teste",
    "valor_por_hora": 50.00,
    "quantidade_horas": 2.5,
    "maquina_id": 1  # ID da máquina associada à manutenção
}
response = post_route("manutencoes", new_manutencao_data)
print("Rota POST /manutencoes:", response)

# Consumindo a rota para obter todas as manutenções
manutencoes = get_route("manutencoes")
print("Rota GET /manutencoes:", manutencoes)

# Consumindo a rota para obter uma manutenção específica
manutencao_id = 1  # ID da manutenção desejada
manutencao = get_route(f"manutencoes/{manutencao_id}")
print(f"Rota GET /manutencoes/{manutencao_id}:", manutencao)

# Consumindo a rota para atualizar uma manutenção específica
update_manutencao_data = {
    "descricao": "Manutenção de teste atualizada",
    "valor_por_hora": 60.00,
    "quantidade_horas": 3.0,
    "data_cadastro": "2024-05-24 10:00:00"  # Data de cadastro atualizada (opcional)
}
response = put_route("manutencoes", manutencao_id, update_manutencao_data)
print(f"Rota PUT /manutencoes/{manutencao_id}:", response)

# Consumindo a rota para deletar uma manutenção específica
response = delete_route("manutencoes", manutencao_id)
print(f"Rota DELETE /manutencoes/{manutencao_id}:", response)

# Consumindo a rota para listar as descrições de manutenção da máquina em ordem decrescente de valor total
maquina_id = 1  # ID da máquina desejada
manutencoes_desc_valor = get_route(f"maquinas/{maquina_id}/manutencoes/desc-valor")
print(f"Rota GET /maquinas/{maquina_id}/manutencoes/desc-valor:", manutencoes_desc_valor)

# Consumindo a rota para exibir as duas últimas manutenções realizadas por uma determinada máquina
ultimas_manutencoes = get_route(f"maquinas/{maquina_id}/manutencoes/ultimas")
print(f"Rota GET /maquinas/{maquina_id}/manutencoes/ultimas:", ultimas_manutencoes)

# Consumindo a rota para listar as manutenções da máquina baseado em um filtro de valor máximo
valor_max = 100.00  # Valor máximo desejado
manutencoes_valor_max = get_route(f"maquinas/{maquina_id}/manutencoes/valor-max/{valor_max}")
print(f"Rota GET /maquinas/{maquina_id}/manutencoes/valor-max/{valor_max}:", manutencoes_valor_max)
