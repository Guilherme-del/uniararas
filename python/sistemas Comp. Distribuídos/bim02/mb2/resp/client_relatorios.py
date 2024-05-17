import paho.mqtt.client as mqtt

broker_address = "localhost"

def on_message_relatorios(client, userdata, message):
    print(f"Relatórios Ambientais recebeu mensagem: {message.topic} -> {message.payload.decode()}")

client_relatorios = mqtt.Client("ClienteRelatorios")
client_relatorios.connect(broker_address)
client_relatorios.subscribe("escritorio/ambiente/qualidade_ar")
client_relatorios.subscribe("escritorio/energia/consumo")
client_relatorios.on_message = on_message_relatorios

client_relatorios.loop_forever()
