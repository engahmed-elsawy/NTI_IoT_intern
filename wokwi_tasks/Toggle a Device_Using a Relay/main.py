from machine import Pin
import time

relay = Pin(26, Pin.OUT)
relay_state = False

button = Pin(14, Pin.IN, Pin.PULL_UP)
last_state = 1

while True:
    current_state = button.value()

    if last_state == 1 and current_state == 0:
        relay_state = not relay_state
        relay.value(relay_state)
        print("Relay is", "ON" if relay_state else "OFF")

        while button.value() == 0:
            time.sleep(0.01)

    last_state = current_state
    time.sleep(0.01)

