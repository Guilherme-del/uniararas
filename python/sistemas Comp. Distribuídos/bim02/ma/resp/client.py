import requests

def create_sensor(nome, tipo, status):
    response = requests.post('http://localhost:5000/sensors', json={'nome': nome, 'tipo': tipo, 'status': status})
    return response.json()

def get_sensors():
    response = requests.get('http://localhost:5000/sensors')
    return response.json()

def update_sensor(sensor_id, nome, tipo, status):
    response = requests.put(f'http://localhost:5000/sensors/{sensor_id}', json={'nome': nome, 'tipo': tipo, 'status': status})
    return response.json()

def delete_sensor(sensor_id):
    response = requests.delete(f'http://localhost:5000/sensors/{sensor_id}')
    return response.json()

def create_casa(endereco, cidade):
    response = requests.post('http://localhost:5000/casas', json={'endereco': endereco, 'cidade': cidade})
    return response.json()

def get_casas():
    response = requests.get('http://localhost:5000/casas')
    return response.json()

def update_casa(casa_id, endereco, cidade):
    response = requests.put(f'http://localhost:5000/casas/{casa_id}', json={'endereco': endereco, 'cidade': cidade})
    return response.json()

def delete_casa(casa_id):
    response = requests.delete(f'http://localhost:5000/casas/{casa_id}')
    return response.json()

def create_comodo(nome, casa_id):
    response = requests.post('http://localhost:5000/comodos', json={'nome': nome, 'casa_id': casa_id})
    return response.json()

def get_comodos():
    response = requests.get('http://localhost:5000/comodos')
    return response.json()

def update_comodo(comodo_id, nome, casa_id):
    response = requests.put(f'http://localhost:5000/comodos/{comodo_id}', json={'nome': nome, 'casa_id': casa_id})
    return response.json()

def delete_comodo(comodo_id):
    response = requests.delete(f'http://localhost:5000/comodos/{comodo_id}')
    return response.json()

def associate_sensor_comodo(sensor_id, comodo_id):
    response = requests.post('http://localhost:5000/associate_sensor_comodo', json={'sensor_id': sensor_id, 'comodo_id': comodo_id})
    return response.json()

if __name__ == '__main__':
    # Testando as funções
    sensor = create_sensor("Sensor de Teste", "Teste", "Ativo")
    print("Sensor criado:", sensor)

    sensors = get_sensors()
    print("Sensores encontrados:", sensors)

    sensor_id = sensors[0]['id']
    updated_sensor = update_sensor(sensor_id, "Novo Nome", "Novo Tipo", "Inativo")
    print("Sensor atualizado:", updated_sensor)

    deleted_sensor = delete_sensor(sensor_id)
    print("Sensor deletado:", deleted_sensor)

    casa = create_casa("Rua Teste, 123", "Cidade Teste")
    print("Casa criada:", casa)

    casas = get_casas()
    print("Casas encontradas:", casas)

    casa_id = casas[0]['id']
    updated_casa = update_casa(casa_id, "Nova Rua, 456", "Nova Cidade")
    print("Casa atualizada:", updated_casa)

    deleted_casa = delete_casa(casa_id)
    print("Casa deletada:", deleted_casa)

    comodo = create_comodo("Quarto", casa_id)
    print("Comodo criado:", comodo)

    comodos = get_comodos()
    print("Comodos encontrados:", comodos)

    comodo_id = comodos[0]['id']
    updated_comodo = update_comodo(comodo_id, "Sala", casa_id)
    print("Comodo atualizado:", updated_comodo)

    deleted_comodo = delete_comodo(comodo_id)
    print("Comodo deletado:", deleted_comodo)

    association = associate_sensor_comodo(sensor_id, comodo_id)
    print("Associação sensor-comodo:", association)
