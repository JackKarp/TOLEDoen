import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1309

from canvasapi import Canvas

def button_callback(channel):
    print("Button was pushed!")
    raise StopException("stop it")

class StopException(Exception):
    def __init__(self, message):
        self.message = message
        print("stopped")

        
api_url_string = "apiurl"
api_key_string = "apikey"

# Reads an "env" file in the canvas folder into a dict. The env file should have "apikey" and "apiurl"
def read_envfile():
    dict = {}
    with open("./canvas/env") as envfile:
        for line in envfile:
            stripped_line = "".join(line.split()).split(":", 1)
            dict[stripped_line[0]] = stripped_line[1] 
    return dict

envdict = read_envfile()
# print(envdict[api_url_string])

def get_content():
    canvas = Canvas(envdict[api_url_string], envdict[api_key_string])
    return canvas.get_courses()

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use number pin numbering
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

GPIO.add_event_detect(15,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge

try:
    serial = spi(port=0, address=0)
    device = ssd1309(serial)
    with canvas(device) as draw:
        draw.text((0,0),get_content()[0].name,fill="white")
        print("drawing")
    message = input("Press enter to quit\n\n") # Run until someone presses enter
except StopException:
    print('excepted')
    device.clear()
finally:
    GPIO.cleanup() # Clean up
