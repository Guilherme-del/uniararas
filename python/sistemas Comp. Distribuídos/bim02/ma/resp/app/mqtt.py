import paho.mqtt.client as mqtt

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

client.on_connect = on_connect

client.connect("mqtt_broker", 1883, 60)
