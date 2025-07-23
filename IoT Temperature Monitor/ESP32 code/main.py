import network
import time
import machine
from umqtt.simple import MQTTClient

SSID = "Wokwi-GUEST"
PASSWORD = ""
MQTT_BROKER = "broker.hivemq.com"
TOPIC_SUB = b"esp32/print"
TOPIC_PUB = b"esp32/temp"
TOPIC_RELAY = b"esp32/relay"  # Relay control topic

# Initialize ADC (e.g., ADC1_CH0 = GPIO36)
adc = machine.ADC(machine.Pin(36))  
adc.atten(machine.ADC.ATTN_11DB)   # Set attenuation for full voltage range (~0 - 3.6V)

# Initialize relay pin (e.g. GPIO15)
relay_pin = machine.Pin(15, machine.Pin.OUT)
relay_pin.value(0)  # Relay initially OFF

def connect_wifi():
    print("Connecting to Wi-Fi...")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        time.sleep(0.1)
    print("Connected, IP:", wlan.ifconfig())

def mqtt_callback(topic, msg):
    print("Topic:", topic, "Message:", msg)

    if topic == TOPIC_RELAY:
        if msg == b'on':
            print("Relay ON")
            relay_pin.value(1)
        elif msg == b'off':
            print("Relay OFF")
            relay_pin.value(0)

def read_temperature():
    # Read ADC raw value and convert to voltage
    adc_val = adc.read()
    voltage = adc_val / 4095 * 3.3  # Assuming 12-bit ADC and 3.3V reference

    # Convert voltage to temperature (example calculation)
    # Adjust formula based on your specific sensor characteristics
    temp_c = (voltage - 0.5) * 100  # For example: 0.5V = 0°C, 10mV per degree C
    return temp_c

def main():
    connect_wifi()
    client = MQTTClient("wokwi-esp32", MQTT_BROKER)
    client.set_callback(mqtt_callback)
    client.connect()
    client.subscribe(TOPIC_SUB)
    client.subscribe(TOPIC_RELAY)
    print("MQTT connected and subscribed")

    last_publish = time.ticks_ms()

    while True:
        client.check_msg()
        if time.ticks_diff(time.ticks_ms(), last_publish) > 10000:
            temp_c = read_temperature()
            temp_str = "{:.2f}".format(temp_c)
            client.publish(TOPIC_PUB, temp_str.encode())
            print(f"Published temperature: {temp_str} °C")
            last_publish = time.ticks_ms()
        time.sleep(0.1)

main()

