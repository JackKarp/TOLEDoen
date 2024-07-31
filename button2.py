import RPi.GPIO as GPIO
from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1309

# Initializes GPIO pins and button detection
device = None
def initialize_device():
    serial = spi(port=0, address=0)

    GPIO.setmode(GPIO.BCM)
    button_pin = 5

    def my_callback(channel):
        print("button")
        raise StopException("StopException: button pressed dummy")

    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=my_callback, bouncetime=300)

    device = ssd1309(serial)
    return device

class StopException(Exception):
    def __init__(self, message):
        self.message = message
        print("stopped")

def render(s, device):
    print("running 2")
    with canvas(device) as draw:
        draw.text((0,0),s,fill="white")
        print("drawing")


def go(s):
    device = initialize_device()
    print("going")
    while True:
        try:
            print("running")
            render(s, device)
        except StopException:
            print("excepted")
            break
        finally:
            GPIO.cleanup()