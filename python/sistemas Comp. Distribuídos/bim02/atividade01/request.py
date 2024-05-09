import requests

base_url = 'http://localhost:5000'

# Função para cadastrar um aluno
def cadastrar_aluno(nome, email, ra, media):
    url = f"{base_url}/cadastrar_aluno"
    data = {
        'nome': nome,
        'email': email,
        'ra': ra,
        'media': media
    }
    response = requests.post(url, json=data)
    print(response.json())

# Função para listar todos os alunos
def listar_alunos():
    url = f"{base_url}/listar_aluno"
    response = requests.get(url)
    print(response.json())

# Função para filtrar um aluno por ID
def filtrar_aluno(id):
    url = f"{base_url}/filtrar_aluno/{id}"
    response = requests.get(url)
    print(response.json())

# Função para atualizar um aluno por ID
def atualizar_aluno(id, nome, email, ra, media):
    url = f"{base_url}/atualizar_aluno"
    data = {
        'id': id,
        'nome': nome,
        'email': email,
        'ra': ra,
        'media': media
    }
    response = requests.put(url, json=data)
    print(response.json())

# Função para deletar um aluno por ID
def deletar_aluno(id):
    url = f"{base_url}/deletar_aluno/{id}"
    response = requests.delete(url)
    print(response.json())

if __name__ == "__main__":
    # utilização das funções
    cadastrar_aluno("João", "joao@example.com", "123456", 8.5)
    cadastrar_aluno("Maria", "maria@example.com", "789012", 9.0)
    listar_alunos()
    filtrar_aluno(1)
    atualizar_aluno(1, "João da Silva", "joao.silva@example.com", "123456", 8.5)
    listar_alunos()
    deletar_aluno(2)
    listar_alunos()
