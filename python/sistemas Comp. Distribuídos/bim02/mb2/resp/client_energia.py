import paho.mqtt.client as mqtt

broker_address = "localhost"

def on_message_energia(client, userdata, message):
    print(f"Gerenciamento de Energia recebeu mensagem: {message.topic} -> {message.payload.decode()}")

client_energia = mqtt.Client("ClienteEnergia")
client_energia.connect(broker_address)
client_energia.subscribe("escritorio/energia/consumo")
client_energia.on_message = on_message_energia

client_energia.loop_forever()
