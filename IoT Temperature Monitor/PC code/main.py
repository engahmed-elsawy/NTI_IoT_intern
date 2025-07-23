import paho.mqtt.client as mqtt

MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
TOPIC_TEMP = "esp32/temp"    # Topic to receive temperature data
TOPIC_RELAY = "esp32/relay"  # Topic to send relay control commands

# Callback when connected to the broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(TOPIC_TEMP)
    print(f"Subscribed to: {TOPIC_TEMP}")

# Callback when a message is received
def on_message(client, userdata, msg):
    if msg.topic == TOPIC_TEMP:
        print(f"Temperature update: {msg.payload.decode()} °C")

client = mqtt.Client("pc-subscriber")
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_start()

try:
    while True:
        msg = input("Type command for relay (on/off) or 'q' to quit: ")
        if msg.lower() == 'q':
            break
        if msg.lower() in ['on', 'off']:
            client.publish(TOPIC_RELAY, msg.lower())
            print(f"Published relay command: {msg.lower()}")
        else:
            print("Unknown command. Please type 'on', 'off' or 'q'.")
except KeyboardInterrupt:
    print("\nInterrupted by user.")
finally:
    client.loop_stop()
    client.disconnect()
    print("Disconnected from broker.")
