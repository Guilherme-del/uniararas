from flask import Flask, request, json
from flask_sqlalchemy import SQLAlchemy
#criamos o app flask e setamos o banco de dados
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///ormdb.db"
#criamos um objeto sqlalchemy
sql = SQLAlchemy(app)

class Aluno(sql.Model):
    id = sql.Column(sql.Integer, primary_key=True, auto_increment=True)
    nome = sql.Column(sql.String, nullable=False)
    ra = sql.Column(sql.String, nullable=False)
    email = sql.Column(sql.String, nullable=False)
    media = sql.Column(sql.Float, nullable=False)

@app.route("/aluno", methods=['POST', 'GET'])
def aluno():
    if request.method == 'POST':
        dados = json.loads(request.data)
        aluno = Aluno(
            nome = dados['nome'],
            ra = dados['ra'],
            email = dados['email'],
            media = dados['media']
        )
        try:
            sql.session.add(aluno)
            sql.session.commit()
            sql.session.refresh(aluno)

            return f"Criado - id: {aluno.id}", 201
        except:
            print("Erro ao inserir!")

@app.route("/alunos")
def listagem_alunos():
    registros = Aluno.query.all()

    response = [
        {
            "id" : aluno.id,
            "nome" : aluno.nome,
            "email": aluno.email,
            "ra" : aluno.ra,
            "media" : aluno.media
        }
        for aluno in registros
    ]

    return { "dados": response }, 200

@app.route("/aluno/<int:id>")
def consultar_aluno_por_id(id):
    aluno = Aluno.query.get(id)
    if aluno:
        response = {
            "id" : aluno.id,
            "nome": aluno.nome,
            "ra" : aluno.ra,
            "media" : aluno.media,
            "email": aluno.email
        }
        return response, 200

    return "Não encontrado", 404

with app.app_context():
    sql.create_all()