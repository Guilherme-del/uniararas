import paho.mqtt.client as mqtt
import json

# Callback chamada quando a conexão ao broker MQTT é estabelecida
def on_connect(client, userdata, flags, rc):
    print("Conectado ao broker MQTT com código de resultado: " + str(rc))
    # Inscreva-se no tópico de log
    client.subscribe("log_audit_maquinas")

# Callback chamada quando uma mensagem é recebida do broker MQTT
def on_message(client, userdata, msg):
    # Decodifique a mensagem JSON
    data = json.loads(msg.payload.decode())
    # Exiba a ação e os dados associados
    print("Ação:", data["action"])
    print("Dados:", data["data"])

# Configuração do cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Conecte-se ao broker MQTT
client.connect("localhost", 1883, 60)

# Mantenha o cliente MQTT em execução para continuar recebendo mensagens
client.loop_forever()
