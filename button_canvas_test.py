import RPi.GPIO as GPIO
from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1309

from canvasapi import Canvas

class StopException(Exception):
    def __init__(self, message):
        self.message = message
        print("stopped")

GPIO.cleanup()
        
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

def render(s):
    print("running 2")
    GPIO.cleanup()
    serial = spi(port=0, address=0)

    # GPIO.setmode(GPIO.BCM)
    button_pin = 5

    def my_callback(channel):
        print("button")
        raise StopException("StopException: button pressed dummy")

    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(button_pin, GPIO.RISING, callback=my_callback, bouncetime=100)

    device = ssd1309(serial)

    with canvas(device) as draw:
        draw.text((0,0),s,fill="white")
        print("drawing")

try:
    render(get_content()[0].name) 
    while True:
        GPIO.wait_for_edge(5,GPIO.RISING)
        
except StopException:
    print("excepted")
finally:
    GPIO.cleanup()