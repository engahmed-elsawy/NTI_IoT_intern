import paho.mqtt.client as mqtt

MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
TOPIC_SUB = "esp32/heartbeat"

# Callback when connected to broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(TOPIC_SUB)
    print(f"Subscribed to {TOPIC_SUB}")

# Callback when a message is received
def on_message(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}")

# Set up client
client = mqtt.Client("pc-subscriber")
client.on_connect = on_connect
client.on_message = on_message
# connect and start loop
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_forever()

