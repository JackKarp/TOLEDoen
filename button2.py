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

def run():
    print("banana")


while butt:
    try:
        run()
    except StopException:
        print("excepted")
        break
    except:
        break
    finally:
        GPIO.cleanup()