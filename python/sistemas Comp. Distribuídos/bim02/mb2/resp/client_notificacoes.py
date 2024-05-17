import paho.mqtt.client as mqtt

broker_address = "localhost"

def on_message_notificacoes(client, userdata, message):
    print(f"Notificações recebeu mensagem: {message.topic} -> {message.payload.decode()}")

client_notificacoes = mqtt.Client("ClienteNotificacoes")
client_notificacoes.connect(broker_address)
client_notificacoes.subscribe("escritorio/salas/ocupacao")
client_notificacoes.on_message = on_message_notificacoes

client_notificacoes.loop_forever()
