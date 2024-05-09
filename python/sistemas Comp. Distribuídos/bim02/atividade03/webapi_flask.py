from flask import Flask, request,json
import sqlite3 as sql
from sqlite3 import Error

def conectar() :
    try:
        con = sql.connect("meubanco.db", check_same_thread=False)
        return con
    except Error as e:
        print("Erro ao conectar - Mensagem:", e)
        
conexao = conectar() #realiza a conexão com o banco para executar os scripts

def criar_tabela() :
    try:
        sql = """
                create table if not exists aluno (
                    id integer primary key autoincrement,
                    nome text,
                    ra text,
                    email text,
                    media numeric
                )
              """
        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()
        print("Tabela criada com sucesso!")
    except Error as e:
        print("Erro ao tentar criar tabela: ", e)

criar_tabela() #cria as tabelas, caso não existam

app = Flask(__name__) #cria o objeto flask 

#Início - Endpoints

@app.route("/aluno", methods=['POST'])
def cadastrar_aluno() :
    dados = json.loads(request.data)
    #criando o script sql para inserir o aluno
    sql = "insert into aluno(nome, ra, email, media) values (?, ?, ?, ?)"

    try:
        cursor = conexao.cursor()
        cursor.execute(sql, (dados['nome'], 
                             dados['ra'], 
                             dados['email'], 
                             dados['media'],))
        
        conexao.commit()
        print("Inserido!")
        return "Inserido", 201
    except Error as e:
        print("Mensagem:", e)
        return "Erro", 500

@app.route("/aluno", methods=['PUT'])
def atualizar_aluno() :
    dados = json.loads(request.data)
    sql = f"""update aluno set nome = '{dados['nome']}', 
                               email = '{dados['email']}', 
                               ra = '{dados['ra']}', 
                               media = {dados['media']} 
            where id = {dados['id']}
          """
    try:
        cursor = conexao.cursor()   
        cursor.execute(sql)
        conexao.commit()
        return "Atualizado!", 200
    except Error as e:
        print("Erro:", e)
        return "Erro", 500

if __name__ == '__main__':
    app.run()