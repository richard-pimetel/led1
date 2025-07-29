from machine import Pin
from utime import sleep

print("Hello World")
led = Pin(15, Pin.OUT)

while True:
    led.on()  
    print("Led ligado!!!")
    sleep(0.5)  
    led.off() 
    print("Led desligado!!!")
    sleep(0.5)  