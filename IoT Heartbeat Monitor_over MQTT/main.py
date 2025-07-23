import machine
import time
import math
import network
from umqtt.simple import MQTTClient  

SSID = "Wokwi-GUEST"
PASSWORD = ""
MQTT_BROKER = "broker.hivemq.com"
TOPIC_PUB = b"esp32/heartbeat"

def connect_wifi():
    print("Connecting to Wi-Fi...")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        time.sleep(0.1)
    print("Connected:", wlan.ifconfig())

def main():
    connect_wifi()
    client = MQTTClient("wokwi-esp32", MQTT_BROKER)
    client.connect()
    print("MQTT connected")

    last_heartbeat = time.ticks_ms()

    while True:
        if time.ticks_diff(time.ticks_ms(), last_heartbeat) > 10000:
            client.publish(TOPIC_PUB, b"I'm alive!")
            print("Sent heartbeat")
            last_heartbeat = time.ticks_ms()
        time.sleep(0.1)

main()
