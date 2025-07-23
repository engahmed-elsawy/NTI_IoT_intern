import machine
import time
import math

BETA = 3950        # BETA configuration
ADC_MAX = 1023     # 10-bit resolution to match Arduino scale
T0 = 298.15        # 25°C in Kelvin

# ADC configuration
adc = machine.ADC(machine.Pin(34))
adc.atten(machine.ADC.ATTN_11DB)
adc.width(machine.ADC.WIDTH_10BIT)

while True:
    analog_value = adc.read()
    if 0 < analog_value < ADC_MAX:
        celsius = 1 / (math.log(1 / (ADC_MAX / analog_value - 1)) / BETA + 1.0 / T0) - 273.15
        print("temp: {:.2f} C".format(celsius))
    else:
        print("Analog value out of range:", analog_value)
    time.sleep(1)  # wait for 1 second


