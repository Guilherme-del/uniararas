import paho.mqtt.client as mqtt
import time
import random

broker_address = "localhost"
client = mqtt.Client("SensorPublisher")
client.connect(broker_address)

def publish_sensor_data():
    while True:
        ocupacao = random.choice(["vazio", "ocupado"])
        qualidade_ar = {"CO2": random.randint(300, 600), "temperatura": random.randint(18, 30), "umidade": random.randint(30, 70)}
        consumo_energia = random.uniform(100.0, 500.0)
        
        client.publish("escritorio/salas/ocupacao", ocupacao)
        client.publish("escritorio/ambiente/qualidade_ar", str(qualidade_ar))
        client.publish("escritorio/energia/consumo", consumo_energia)
        
        time.sleep(5)

publish_sensor_data()
