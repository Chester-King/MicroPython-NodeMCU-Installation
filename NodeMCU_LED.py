import time
import machine

pin = machine.Pin(14, machine.Pin.OUT)  # D5


while(True):
    pin.on()
    time.sleep(1)
    pin.off()
    time.sleep(2)
