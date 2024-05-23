from flask import request, jsonify
from . import db
from .models import Sensor, Casa, Comodo, ComodoXSensores
import paho.mqtt.publish as publish

def publish_mqtt(message):
    publish.single("sensores", payload=message, hostname="localhost", port=1883)

def register_routes(app):
    # Sensor CRUD
    @app.route('/sensors', methods=['POST'])
    def create_sensor():
        data = request.get_json()
        new_sensor = Sensor(nome=data['nome'], tipo=data['tipo'], status=data['status'])
        db.session.add(new_sensor)
        db.session.commit()
        publish_mqtt(f"Sensor created with id {new_sensor.id}")
        return jsonify({'message': 'Sensor created'})

    @app.route('/sensors', methods=['GET'])
    def get_sensors():
        sensors = Sensor.query.all()
        result = [{'id': sensor.id, 'nome': sensor.nome, 'tipo': sensor.tipo, 'status': sensor.status} for sensor in sensors]
        publish_mqtt("Fetched all sensors")
        return jsonify(result)

    @app.route('/sensors/<int:sensor_id>', methods=['PUT'])
    def update_sensor(sensor_id):
        data = request.get_json()
        sensor = Sensor.query.get_or_404(sensor_id)
        sensor.nome = data['nome']
        sensor.tipo = data['tipo']
        sensor.status = data['status']
        db.session.commit()
        publish_mqtt(f"Sensor with id {sensor.id} updated")
        return jsonify({'message': 'Sensor updated'})

    @app.route('/sensors/<int:sensor_id>', methods=['DELETE'])
    def delete_sensor(sensor_id):
        sensor = Sensor.query.get_or_404(sensor_id)
        db.session.delete(sensor)
        db.session.commit()
        publish_mqtt(f"Sensor with id {sensor.id} deleted")
        return jsonify({'message': 'Sensor deleted'})

    # Casa CRUD
    @app.route('/casas', methods=['POST'])
    def create_casa():
        data = request.get_json()
        new_casa = Casa(endereco=data['endereco'], cidade=data['cidade'])
        db.session.add(new_casa)
        db.session.commit()
        publish_mqtt(f"Casa created with id {new_casa.id}")
        return jsonify({'message': 'Casa created'})

    @app.route('/casas', methods=['GET'])
    def get_casas():
        casas = Casa.query.all()
        result = [{'id': casa.id, 'endereco': casa.endereco, 'cidade': casa.cidade} for casa in casas]
        publish_mqtt("Fetched all casas")
        return jsonify(result)

    @app.route('/casas/<int:casa_id>', methods=['PUT'])
    def update_casa(casa_id):
        data = request.get_json()
        casa = Casa.query.get_or_404(casa_id)
        casa.endereco = data['endereco']
        casa.cidade = data['cidade']
        db.session.commit()
        publish_mqtt(f"Casa with id {casa.id} updated")
        return jsonify({'message': 'Casa updated'})

    @app.route('/casas/<int:casa_id>', methods=['DELETE'])
    def delete_casa(casa_id):
        casa = Casa.query.get_or_404(casa_id)
        db.session.delete(casa)
        db.session.commit()
        publish_mqtt(f"Casa with id {casa.id} deleted")
        return jsonify({'message': 'Casa deleted'})

    # Comodo CRUD
    @app.route('/comodos', methods=['POST'])
    def create_comodo():
        data = request.get_json()
        new_comodo = Comodo(nome=data['nome'], casa_id=data['casa_id'])
        db.session.add(new_comodo)
        db.session.commit()
        publish_mqtt(f"Comodo created with id {new_comodo.id}")
        return jsonify({'message': 'Comodo created'})

    @app.route('/comodos', methods=['GET'])
    def get_comodos():
        comodos = Comodo.query.all()
        result = [{'id': comodo.id, 'nome': comodo.nome, 'casa_id': comodo.casa_id} for comodo in comodos]
        publish_mqtt("Fetched all comodos")
        return jsonify(result)

    @app.route('/comodos/<int:comodo_id>', methods=['PUT'])
    def update_comodo(comodo_id):
        data = request.get_json()
        comodo = Comodo.query.get_or_404(comodo_id)
        comodo.nome = data['nome']
        comodo.casa_id = data['casa_id']
        db.session.commit()
        publish_mqtt(f"Comodo with id {comodo.id} updated")
        return jsonify({'message': 'Comodo updated'})

    @app.route('/comodos/<int:comodo_id>', methods=['DELETE'])
    def delete_comodo(comodo_id):
        comodo = Comodo.query.get_or_404(comodo_id)
        db.session.delete(comodo)
        db.session.commit()
        publish_mqtt(f"Comodo with id {comodo.id} deleted")
        return jsonify({'message': 'Comodo deleted'})

    # Associate Sensor with Comodo
    @app.route('/associate_sensor_comodo', methods=['POST'])
    def associate_sensor_comodo():
        data = request.get_json()
        comodo_id = data['comodo_id']
        sensor_id = data['sensor_id']
        new_association = ComodoXSensores(sensor_id=sensor_id, comodo_id=comodo_id)
        db.session.add(new_association)
        db.session.commit()
        publish_mqtt(f"Associated sensor {sensor_id} with comodo {comodo_id}")
        return jsonify({'message': 'Sensor associated with comodo'})
