from flask import Flask, request, jsonify
import sqlite3
from sqlite3 import Error

# Criando o servidor Flask
servidor = Flask(__name__)

def create_connection(db_file):
    """ 
    Cria uma conexão com o banco de dados SQLite especificado pelo db_file 
    :param db_file: arquivo do banco de dados 
    :return: conexão com o banco de dados ou None em caso de falha 
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

# Caminho do arquivo do banco de dados
database = 'primeiro.db'

# Criação de uma conexão global com o banco de dados
global_conn = create_connection(database)

def create_table():
    """
    Cria uma tabela chamada 'aluno' no banco de dados, se ainda não existir.
    """
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS aluno (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        ra TEXT NOT NULL,
        media REAL NOT NULL
    );
    """
    try:
        # Obtém um cursor para executar comandos SQL
        cursor = global_conn.cursor()
        # Executa o comando SQL para criar a tabela
        cursor.execute(create_table_sql)
        # Confirma a execução da transação
        global_conn.commit()
        # Fecha o cursor
        cursor.close()
    except Error as e:
        print(e)

# Chamada da função para criar a tabela no escopo global
create_table()

class Aluno:
    def __init__(self, nome, email, ra, media):
        self.nome = nome
        self.email = email
        self.ra = ra
        self.media = media

# Definindo o endpoint /home
@servidor.route('/home')
def home():
    return 'Servidor em execução'

# Definindo o endpoint /cadastrar_aluno
@servidor.route('/cadastrar_aluno', methods=['POST'])
def cadastrar_aluno():
    # Recebe os dados do aluno do corpo da requisição
    dados = request.get_json()
    # Instancia um objeto da classe Aluno com as informações recebidas
    aluno = Aluno(dados['nome'], dados['email'], dados['ra'], dados['media'])
    
    # Script SQL para inserir o aluno no banco de dados
    sql = "INSERT INTO aluno (nome, email, ra, media) VALUES (?, ?, ?, ?)"
    try:
        # Obtém um cursor para executar comandos SQL
        cursor = global_conn.cursor()
        # Executa o comando SQL para inserir o aluno
        cursor.execute(sql, (aluno.nome, aluno.email, aluno.ra, aluno.media))
        # Confirma a execução da transação
        global_conn.commit()
        # Fecha o cursor
        cursor.close()
        # Retorna uma mensagem indicando que o aluno foi incluído na base de dados
        return jsonify({'mensagem': 'Novo aluno incluído na base de dados.'}), 201
    except Error as e:
        print(e)
        return jsonify({'erro': 'Ocorreu um erro ao inserir o aluno na base de dados.'}), 500

# Função para deletar um aluno do banco de dados
def deletar_aluno(id):
    sql = "DELETE FROM aluno WHERE id = ?"
    try:
        cursor = global_conn.cursor()
        cursor.execute(sql, (id,))
        global_conn.commit()
        cursor.close()
    except Error as e:
        print(e)

# Definindo o endpoint /deletar_aluno
@servidor.route("/deletar_aluno/<int:id>", methods=["DELETE"])
def deletar_aluno_endpoint(id):
    deletar_aluno(id)
    return jsonify({'mensagem': f'Aluno com ID {id} deletado.'}), 200

# Definindo o endpoint /listar_aluno
@servidor.route('/listar_aluno')
def listar_aluno():
    # Script SQL para selecionar todos os alunos da tabela aluno
    sql = "SELECT * FROM aluno"
    try:
        # Obtém um cursor para executar comandos SQL
        cursor = global_conn.cursor()
        # Executa o comando SQL para selecionar todos os alunos
        alunos = cursor.execute(sql).fetchall()
        # Fecha o cursor
        cursor.close()
        # Lista para armazenar os dados dos alunos
        lista_alunos = []
        # Itera sobre os alunos retornados do banco de dados
        for aluno in alunos:
            # Dicionário para armazenar as informações de um aluno
            aluno_info = {
                'id': aluno[0],
                'nome': aluno[1],
                'email': aluno[2],
                'ra': aluno[3],
                'media': aluno[4]
            }
            # Adiciona as informações do aluno à lista de alunos
            lista_alunos.append(aluno_info)
        # Retorna o dicionário com os alunos e suas respectivas informações
        return jsonify({'alunos': lista_alunos}), 200
    except Error as e:
        print(e)
        return jsonify({'erro': 'Ocorreu um erro ao listar os alunos.'}), 500

# Definindo o endpoint /filtrar_aluno
@servidor.route("/filtrar_aluno/<int:id>")
def filtrar_aluno(id):
    # Script SQL para selecionar um único aluno com base no ID fornecido
    sql = "SELECT * FROM aluno WHERE id = ?"
    try:
        # Obtém um cursor para executar comandos SQL
        cursor = global_conn.cursor()
        # Executa o comando SQL para selecionar o aluno com base no ID
        aluno = cursor.execute(sql, (id,)).fetchone()
        # Fecha o cursor
        cursor.close()
        # Se não encontrar o aluno, retorna um erro 404
        if aluno is None:
            return jsonify({'erro': 'Aluno não encontrado.'}), 404
        # Caso contrário, retorna as informações do aluno encontrado
        aluno_info = {
            'id': aluno[0],
            'nome': aluno[1],
            'email': aluno[2],
            'ra': aluno[3],
            'media': aluno[4]
        }
        return jsonify(aluno_info), 200
    except Error as e:
        print(e)
        return jsonify({'erro': 'Ocorreu um erro ao filtrar o aluno.'}), 500

# Definindo o endpoint /atualizar_aluno
@servidor.route("/atualizar_aluno", methods=["PUT"])
def atualizar_aluno():
    # Recebe os dados atualizados do aluno do corpo da requisição
    dados = request.get_json()
    # Extrai o ID do aluno dos dados recebidos
    id_aluno = dados['id']
    # Verifica se o aluno com o ID fornecido existe no banco de dados
    aluno_existente = filtrar_aluno(id_aluno)
    if aluno_existente.status_code != 200:
        return jsonify({'erro': 'Aluno não encontrado.'}), 404
    # Atualiza as informações do aluno no banco de dados
    sql = "UPDATE aluno SET nome = ?, email = ?, ra = ?, media = ? WHERE id = ?"
    try:
        # Obtém um cursor para executar comandos SQL
        cursor = global_conn.cursor()
        # Executa o comando SQL para atualizar o aluno
        cursor.execute(sql, (dados['nome'], dados['email'], dados['ra'], dados['media'], id_aluno))
        # Confirma a execução da transação
        global_conn.commit()
        # Fecha o cursor
        cursor.close()
        # Retorna uma mensagem indicando que o aluno foi atualizado na base de dados
        return jsonify({'mensagem': 'Informações do aluno atualizadas com sucesso.'}), 200
    except Error as e:
        print(e)
        return jsonify({'erro': 'Ocorreu um erro ao atualizar as informações do aluno.'}), 500

if __name__ == '__main__':
    # Inicia o servidor Flask
    servidor.run()
