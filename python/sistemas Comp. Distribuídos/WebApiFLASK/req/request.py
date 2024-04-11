import requests

# Listar produtos do carrinho de um usuário
response = requests.get('http://localhost:5000/usuarios/marcilio/carrinho')
print(response.json())

# Remover produto do carrinho de um usuário
response = requests.delete('http://localhost:5000/usuarios/marcilio/carrinho/22')
print(response.json())

# Adicionar produto ao carrinho de um usuário
data = {
    'codigo': 5,
    'nome': 'caderno',
    'valor': 15.00
}
response = requests.post('http://localhost:5000/usuarios/marcilio/carrinho', json=data)
print(response.json())

# Atualizar nome do usuário
data = {'nome': 'Marcilio F. Oliveira'}
response = requests.put('http://localhost:5000/usuarios/marcilio', json=data)
print(response.json())

# Criar um novo usuário
data = {
    'usuario': 'novo_usuario',
    'nome': 'Novo Usuário',
    'id': 2,
    'carrinho': {'total': 0, 'produtos': []}
}
response = requests.post('http://localhost:5000/usuarios', json=data)
print(response.json())

# Total de usuários existentes
response = requests.get('http://localhost:5000/usuarios/total')
print(response.json())

# Somatória de todos os carrinhos existentes
response = requests.get('http://localhost:5000/carrinhos/total')
print(response.json())
