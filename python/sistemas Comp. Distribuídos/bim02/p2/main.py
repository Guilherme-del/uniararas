from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import paho.mqtt.publish as publish
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Configurações MQTT
MQTT_BROKER = "localhost"  # Endereço do broker MQTT
MQTT_PORT = 1883  #Q Porta do broker MTT
MQTT_TOPIC = "log_audit_maquinas"  # Tópico MQTT para publicação de logs

class Maquina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(50), unique=True, nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    manutencoes = db.relationship('Manutencao', backref='maquina', lazy=True)

class Manutencao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200), nullable=False)
    valor_por_hora = db.Column(db.Float, nullable=False)
    quantidade_horas = db.Column(db.Float, nullable=False)
    data_cadastro = db.Column(db.DateTime, default=datetime.utcnow)
    maquina_id = db.Column(db.Integer, db.ForeignKey('maquina.id'), nullable=False)

@app.before_request
def create_tables():
    db.create_all()

# Função para publicar logs via MQTT
def publish_mqtt_log(data):
    publish.single(MQTT_TOPIC, json.dumps(data), hostname=MQTT_BROKER, port=MQTT_PORT)

@app.route('/maquinas', methods=['POST'])
def create_maquina():
    data = request.get_json()
    new_maquina = Maquina(codigo=data['codigo'], descricao=data['descricao'], tipo=data['tipo'])
    db.session.add(new_maquina)
    db.session.commit()
    publish_mqtt_log({"action": "create_maquina", "data": data})
    return jsonify({"message": "Máquina criada com sucesso!"}), 201

@app.route('/maquinas', methods=['GET'])
def get_maquinas():
    maquinas = Maquina.query.all()
    result = []
    for maquina in maquinas:
        maquina_data = {"id": maquina.id, "codigo": maquina.codigo, "descricao": maquina.descricao, "tipo": maquina.tipo, "manutencoes": [manutencao.id for manutencao in maquina.manutencoes]}
        result.append(maquina_data)

    publish_mqtt_log({"action": "get_maquinas", "data": result})
    return jsonify(result)

@app.route('/maquinas/<int:id>', methods=['GET'])
def get_maquina(id):
    maquina = Maquina.query.get_or_404(id)
    maquina_data = {"id": maquina.id, "codigo": maquina.codigo, "descricao": maquina.descricao, "tipo": maquina.tipo, "manutencoes": [manutencao.id for manutencao in maquina.manutencoes]}
   
    publish_mqtt_log({"action": "get_specific_maquina", "data": maquina_data})
    return jsonify(maquina_data)

@app.route('/maquinas/<int:id>', methods=['PUT'])
def update_maquina(id):
    data = request.get_json()
    maquina = Maquina.query.get_or_404(id)
    maquina.codigo = data['codigo']
    maquina.descricao = data['descricao']
    maquina.tipo = data['tipo']
    db.session.commit()

    publish_mqtt_log({"action": "update_maquinas", "data": data})
    return jsonify({"message": "Máquina atualizada com sucesso!"})

@app.route('/maquinas/<int:id>', methods=['DELETE'])
def delete_maquina(id):
    maquina = Maquina.query.get_or_404(id)
    db.session.delete(maquina)
    db.session.commit()

    publish_mqtt_log({"action": "delete_maquina", "data": id})
    return jsonify({"message": "Máquina deletada com sucesso!"})

@app.route('/manutencoes', methods=['POST'])
def create_manutencao():
    data = request.get_json()
    new_manutencao = Manutencao(
        descricao=data['descricao'],
        valor_por_hora=data['valor_por_hora'],
        quantidade_horas=data['quantidade_horas'],
        maquina_id=data['maquina_id']
    )
    db.session.add(new_manutencao)
    db.session.commit()

    publish_mqtt_log({"action": "create_manutencao", "data": new_manutencao.id})
    return jsonify({"message": "Manutenção criada com sucesso!"}), 201

@app.route('/manutencoes', methods=['GET'])
def get_manutencoes():
    manutencoes = Manutencao.query.all()
    result = []
    for manutencao in manutencoes:
        manutencao_data = {
            "id": manutencao.id,
            "descricao": manutencao.descricao,
            "valor_por_hora": manutencao.valor_por_hora,
            "quantidade_horas": manutencao.quantidade_horas,
            "data_cadastro": manutencao.data_cadastro,
            "maquina_id": manutencao.maquina_id
        }
        result.append(manutencao_data)

    publish_mqtt_log({"action": "get_manutencao", "data": result})    
    return jsonify(result)

@app.route('/manutencoes/<int:id>', methods=['GET'])
def get_manutencao(id):
    manutencao = Manutencao.query.get_or_404(id)
    manutencao_data = {
        "id": manutencao.id,
        "descricao": manutencao.descricao,
        "valor_por_hora": manutencao.valor_por_hora,
        "quantidade_horas": manutencao.quantidade_horas,
        "data_cadastro": manutencao.data_cadastro,
        "maquina_id": manutencao.maquina_id
    }
    publish_mqtt_log({"action": "get_specific_manutencao", "data": manutencao_data})    
    return jsonify(manutencao_data)

@app.route('/manutencoes/<int:id>', methods=['PUT'])
def update_manutencao(id):
    data = request.get_json()
    manutencao = Manutencao.query.get_or_404(id)
    manutencao.descricao = data['descricao']
    manutencao.valor_por_hora = data['valor_por_hora']
    manutencao.quantidade_horas = data['quantidade_horas']
    manutencao.data_cadastro = datetime.strptime(data['data_cadastro'], '%Y-%m-%d %H:%M:%S') if 'data_cadastro' in data else manutencao.data_cadastro
    db.session.commit()

    publish_mqtt_log({"action": "update_manutencao", "data": manutencao})    
    return jsonify({"message": "Manutenção atualizada com sucesso!"})

@app.route('/manutencoes/<int:id>', methods=['DELETE'])
def delete_manutencao(id):
    manutencao = Manutencao.query.get_or_404(id)
    db.session.delete(manutencao)
    db.session.commit()

    publish_mqtt_log({"action": "delete_manutencao", "data": manutencao})    
    return jsonify({"message": "Manutenção deletada com sucesso!"})

#  Listagem das descrições de manutenção da máquina em ordem decrescente de valor total (valor por hora * quantidade de horas)
@app.route('/maquinas/<int:maquina_id>/manutencoes/desc-valor', methods=['GET'])
def get_manutencoes_desc_valor(maquina_id):
    manutencoes = Manutencao.query.filter_by(maquina_id=maquina_id).order_by(
        (Manutencao.valor_por_hora * Manutencao.quantidade_horas).desc()
    ).all()
    result = [{"id": m.id, "descricao": m.descricao, "valor_total": m.valor_por_hora * m.quantidade_horas} for m in manutencoes]
    publish_mqtt_log({"action": "list_maquina_description", "data": result})    
    return jsonify(result)

#Exibição das duas últimas manutenções realizadas por uma determinada máquina
@app.route('/maquinas/<int:maquina_id>/manutencoes/ultimas', methods=['GET'])
def get_ultimas_manutencoes(maquina_id):
    manutencoes = Manutencao.query.filter_by(maquina_id=maquina_id).order_by(
        Manutencao.data_cadastro.desc()
    ).limit(2).all()
    result = [{"id": m.id, "descricao": m.descricao, "data_cadastro": m.data_cadastro} for m in manutencoes]
    
    publish_mqtt_log({"action": "show_last_maquinas", "data": result})    
    return jsonify(result)

# Listagem das manutenções da máquina baseado em um filtro de valor máximo
@app.route('/maquinas/<int:maquina_id>/manutencoes/valor-max/<float:valor_max>', methods=['GET'])
def get_manutencoes_valor_max(maquina_id, valor_max):
    manutencoes = Manutencao.query.filter_by(maquina_id=maquina_id).filter(
        (Manutencao.valor_por_hora * Manutencao.quantidade_horas) <= valor_max
    ).all()
    result = [{"id": m.id, "descricao": m.descricao, "valor_total": m.valor_por_hora * m.quantidade_horas} for m in manutencoes]
    
    publish_mqtt_log({"action": "list_based_filter", "data": result})    
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
