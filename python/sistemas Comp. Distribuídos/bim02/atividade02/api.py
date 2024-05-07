from flask import Flask, request, json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
db = SQLAlchemy(app)


class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    ra = db.Column(db.String(20))
    email = db.Column(db.String(100))
    media = db.Column(db.Numeric)

    disciplinas = db.relationship('Disciplina', secondary='aluno_disciplina', backref='alunos')


class Disciplina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    descricao = db.Column(db.String(255))


# Tabela de associação entre Aluno e Disciplina
aluno_disciplina = db.Table('aluno_disciplina',
                            db.Column('aluno_id', db.Integer, db.ForeignKey('aluno.id')),
                            db.Column('disciplina_id', db.Integer, db.ForeignKey('disciplina.id'))
                            )


# Endpoint para permitir que um aluno se inscreva em uma disciplina
@app.route("/aluno/inscrever-disciplina", methods=['POST'])
def inscrever_disciplina():
    dados = json.loads(request.data)
    aluno_id = dados.get('aluno_id')
    disciplina_id = dados.get('disciplina_id')

    aluno = Aluno.query.get(aluno_id)
    disciplina = Disciplina.query.get(disciplina_id)

    if aluno and disciplina:
        aluno.disciplinas.append(disciplina)
        db.session.commit()
        return "Aluno inscrito na disciplina com sucesso!", 201
    else:
        return "Aluno ou disciplina não encontrados", 404


# Endpoint para consultar as disciplinas de um determinado aluno
@app.route("/aluno/disciplinas/<int:aluno_id>", methods=['GET'])
def consultar_disciplinas(aluno_id):
    aluno = Aluno.query.get(aluno_id)
    if aluno:
        disciplinas = [disciplina.nome for disciplina in aluno.disciplinas]
        return json.dumps(disciplinas), 200
    else:
        return "Aluno não encontrado", 404


# Endpoint para cadastrar um aluno
@app.route("/aluno", methods=['POST'])
def cadastrar_aluno():
    dados = json.loads(request.data)

    sql = "insert into aluno(nome, ra, email, media) values (?, ?, ?, ?)"

    try:
        cursor = conexao.cursor()  # Criando um novo cursor
        cursor.execute(sql, (dados['nome'],
                             dados['ra'],
                             dados['email'],
                             dados['media'],))  # Executando o insert na base de dados

        conexao.commit()  # Confirmando a transação
        print("Inserido!")
        return "Inserido", 201
    except Error as e:
        print("Mensagem:", e)
        return "Erro", 500


# Endpoint para atualizar um aluno
@app.route("/aluno", methods=['PUT'])
def atualizar_aluno():
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


# Endpoint para listar todos os alunos
@app.route("/aluno", methods=['GET'])
def listar_aluno():
    sql = f"""select * from aluno 
          """
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        alunos = cursor.fetchall()  # Retorna todos os registros da tabela
        return json.dumps(alunos), 200
    except Error as e:
        print("Erro:", e)
        return "Erro", 500


# Endpoint para deletar um aluno
@app.route("/aluno", methods=['DELETE'])
def deletar_aluno():
    dados = json.loads(request.data)
    sql = f"""delete from aluno where id = {dados['id']}
          """
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()
        return "Deletado!", 200
    except Error as e:
        print("Erro:", e)
        return "Erro", 500


# Endpoint para filtrar um aluno por ID
@app.route("/aluno/filtro", methods=['POST'])
def filtrar_aluno():
    dados = json.loads(request.data)

    sql = f"""select * from aluno where id = {dados['id']}
          """

    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
        aluno = cursor.fetchone()  # Retorna apenas o primeiro registro que atender a condicao
        print(aluno)
        return json.dumps(aluno), 200
    except Error as e:
        print("Erro:", e)
        return "Erro", 500


if __name__ == '__main__':
    db.create_all()
    app.run()
