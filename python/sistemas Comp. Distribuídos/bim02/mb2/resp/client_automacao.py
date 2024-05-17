import paho.mqtt.client as mqtt

broker_address = "localhost"

def on_message_automacao(client, userdata, message):
    print(f"Automação recebeu mensagem: {message.topic} -> {message.payload.decode()}")

client_automacao = mqtt.Client("ClienteAutomacao")
client_automacao.connect(broker_address)
client_automacao.subscribe("escritorio/salas/ocupacao")
client_automacao.subscribe("escritorio/ambiente/qualidade_ar")
client_automacao.on_message = on_message_automacao

client_automacao.loop_forever()
