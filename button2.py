import RPi.GPIO as GPIO
from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1309

serial = spi(port=0, address=0)
device = ssd1309(serial)

GPIO.setmode(GPIO.BCM)
button_pin = 5

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
butt = True

class StopException(Exception):
    def __init__(self, message):
        self.message = message
        print("stopped")


def my_callback(channel):
    print("button")
    butt = False
    raise StopException("StopException: button pressed dummy")

GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=my_callback, bouncetime=300)

def run(s):
    print("running 2")
    with canvas(device) as draw:
        draw.text((0,0),s,fill="white")
        print("drawing")


def go(s):
    GPIO.setmode(GPIO.BCM)
    button_pin = 5

    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    butt = True
    print("going")
    while butt:
        try:
            print("running")
            run(s)
        except StopException:
            print("excepted")
            break
        finally:
            GPIO.cleanup()