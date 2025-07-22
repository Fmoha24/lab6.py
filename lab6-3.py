import time
from adafruit_circuitplayground import cp

def CelToFahr(celsius):
    return celsius * 9 / 5 + 32

def FahrToCell(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

while True:
    if cp.button_a:
        temp_c = cp.temperature
        if cp.switch:  # slider True = convert Celsius to Fahrenheit
            temp = CelToFahr(temp_c)
            print("Temperature in Fahrenheit:", temp)
        else:          # slider False = convert Fahrenheit to Celsius
            temp_f = CelToFahr(temp_c)
            temp = FahrToCell(temp_f)
            print("Temperature in Celsius:", temp)
    time.sleep(0.1)
