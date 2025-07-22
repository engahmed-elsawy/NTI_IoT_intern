from machine import Pin 
import time         

# Define LED pins
# Connect these to your LEDs via resistors
led1y = Pin(26, Pin.OUT)
led2b = Pin(27, Pin.OUT)
led3g = Pin(14, Pin.OUT)
led4r = Pin(12, Pin.OUT)
leds = [led1y, led2b, led3g, led4r]
start_button = Pin(21, Pin.IN, Pin.PULL_UP)
stop_button = Pin(19, Pin.IN, Pin.PULL_UP)

for led in leds:
    led.value(0) 

blinking_active = False 
current_led_index = 0   
while True:
    if start_button.value() == 0 and not blinking_active: # set the flag
        blinking_active = True
        for led in leds:
            led.value(0)
        current_led_index = 0 

    if stop_button.value() == 0 and blinking_active: # unset the flag
        blinking_active = False
        for led in leds:
            led.value(0)
        time.sleep(0.2) 

    if blinking_active: # blinking 
        
        for led in leds:
            led.value(0)

        leds[current_led_index].value(1) 
        time.sleep(1)

                            # index = 0 , 1 , 2 , 3 -> 0 ,1 ,2, 3
        current_led_index = (current_led_index + 1) % len(leds)
    else:
       
        time.sleep(0.01)

