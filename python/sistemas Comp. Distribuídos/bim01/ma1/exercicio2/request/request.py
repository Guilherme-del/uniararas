import requests

# Exemplo de requisição GET para listar todos os produtos
response = requests.get('http://localhost:5000/produtos')
print(response.json())

# Exemplo de requisição GET para obter um produto específico (supondo que o produto com ID 1 exista)
response = requests.get('http://localhost:5000/produtos/1')
print(response.json())
# Exemplo de requisição POST para adicionar um novo produto
novo_produto = {"nome": "Novo Produto", "descricao": "Descrição do Novo Produto", "preco": 30.0}
response = requests.post('http://localhost:5000/produtos', json=novo_produto)
print(response.json())
# Exemplo de requisição PUT para atualizar um produto existente (supondo que o produto com ID 1 exista)
dados_atualizados = {"nome": "Produto Atualizado", "descricao": "Descrição Atualizada", "preco": 25.0}
response = requests.put('http://localhost:5000/produtos/1', json=dados_atualizados)
print(response.json())
# Exemplo de requisição DELETE para remover um produto existente (supondo que o produto com ID 1 exista)
response = requests.delete('http://localhost:5000/produtos/2')
print(response.json())
