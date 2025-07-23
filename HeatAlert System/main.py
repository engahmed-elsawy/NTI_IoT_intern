import machine
import time
import math

# Constants
BETA = 3950        # BETA configuration
ADC_MAX = 1023     # 10-bit ADC resolution
T0 = 298.15        # 25°C in Kelvin
THRESHOLD = 35.0   # Threshold temp in Celsius for LED warning

# ADC setup
adc = machine.ADC(machine.Pin(34))
adc.atten(machine.ADC.ATTN_11DB)
adc.width(machine.ADC.WIDTH_10BIT)

# LED setup
led = machine.Pin(2, machine.Pin.OUT)  # GPIO 2 as output for LED

while True:
    analog_value = adc.read()
    
    if 0 < analog_value < ADC_MAX:
        celsius = 1 / (math.log(1 / (ADC_MAX / analog_value - 1)) / BETA + 1.0 / T0) - 273.15
        print("temp: {:.2f} C".format(celsius))
        
        # LED on/off control
        if celsius > THRESHOLD:
            led.value(1)  # turn LED on
        else:
            led.value(0)  # turn LED off
    else:
        print("Analog value out of range:", analog_value)
        led.value(0)  # turn off LED if invalid reading
    
    time.sleep(1)



