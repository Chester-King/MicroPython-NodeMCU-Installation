# MICROPYTHON-NODEMCU

This is a step by step installation guide on how to run micropython on NodeMCU and a sample Blink micropython code

## Installing

- You would first need NodeMCU-PyFlasher to flash the NodeMCU with the required firmware. You can download NodeMCU-Pyflasher for your machine from [here](https://github.com/marcelstoer/nodemcu-pyflasher/releases). You can directly get the executable file from [here for 64-bit](https://github.com/marcelstoer/nodemcu-pyflasher/releases/download/v4.0/NodeMCU-PyFlasher-4.0-x64.exe) and [here for 32-bit](https://github.com/marcelstoer/nodemcu-pyflasher/releases/download/v4.0/NodeMCU-PyFlasher-4.0-x86.exe). For Mac you can get the dmg file from [here for dmg](https://github.com/marcelstoer/nodemcu-pyflasher/releases/download/v4.0/NodeMCU-PyFlasher-4.0.dmg). You can also get the source code from [here - zip file](https://github.com/marcelstoer/nodemcu-pyflasher/archive/v4.0.zip) and [here - tar.gz file](https://github.com/marcelstoer/nodemcu-pyflasher/archive/v4.0.tar.gz)
- You would also need the MicroPython firmware for ESP8266 to flash the NodeMCU with it. You can either directly download it from [here](http://micropython.org/resources/firmware/esp8266-20191220-v1.12.bin) or can go to the [MicroPython Download Section](http://micropython.org/download) and get it yourself. I recommend you download a stable firmware.
- You will also be needing ESPlorer to write MicroPython code and run it on NodeMCU. You can get it from [here](https://esp8266.ru/esplorer/) or you can just download form [here](http://esp8266.ru/esplorer-latest/?f=ESPlorer.zip). If you want to take a look at their source code, you can do so from [here](https://github.com/4refr0nt/ESPlorer).
- You should have the latest Java version on your system to run the ESPlorer. You can get Java from [here](https://www.java.com/en/download/win10.jsp)

## Getting Started

- First you need to Flash the NodeMCU with the MicroPython Firmware. For this Open the NodeMCU-PyFlasher and select the firmware from where you downloaded it. Make sure **Erase flash** setting is set to yes. ![Image1](https://github.com/Chester-King/MicroPython-NodeMCU-Installation/blob/master/Images/Flasher.png)
- Run the ESPlorer.bat file in the ESPlorer folder. That will execute a series of commands for you which will be used to run ESPlorer. ![Image2](https://github.com/Chester-King/MicroPython-NodeMCU-Installation/blob/master/Images/cli.png) ![Image3](https://github.com/Chester-King/MicroPython-NodeMCU-Installation/blob/master/Images/espl.png)
- After this click on Open in ESPlorer while NodeMCU is connected to your machine. Then while it is Open RESET the NodeMCU. ![Image4](https://pbs.twimg.com/media/CgrGCrRUgAAOcvn.jpg)

## Writing MicroPython Code

You can now write basic MicroPython code in the ESPlorer. Sample Blink Code:

```python
import time
import machine

pin=machine.Pin(14,machine.Pin.OUT)

pin1=machine.Pin(2,machine.Pin.OUT)
pin2=machine.Pin(16,machine.Pin.OUT)

while(True):
    pin1.on()
    time.sleep(1)
    pin1.off()
    time.sleep(2)
```

## Sending the code to ESP

Just click on `Send to ESP` and the code will execute in your NodeMCU. You will be able to see the NodeMCU LED Blinking.
![Image4](https://github.com/Chester-King/MicroPython-NodeMCU-Installation/blob/master/Images/demp.jpeg)
