# Do everything overall
# List of Pages: Off, Clock, Canvas, Weather

from page import Page
from page_machine import PageMachine

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1309

from clock import run_clock, posn
import canvas
from off import clear_display

print("Running main")

button_pin = 15

# TODO: make each of these pages have an on_enter_func
# TODO: refactor clock to be button-interruptible
# TODO: Find some way to wait for callbacks to cycle


# Makes a list of the pages for the page machine
def make_page_list():
    page_list = []


    page_list.append(Page("Off", on_enter_func= lambda x: clear_display))
    page_list.append(Page("Clock", on_enter_func= run_clock, is_flaggable=True))
    page_list.append(Page("Canvas", on_enter_func=canvas.run_canvas))
    page_list.append(Page("Weather", on_enter_func=lambda x: print("placeholder")))
    return page_list

def clean_cycle(pin):
    GPIO.cleanup()
    init_pins(pin)
    GPIO.add_event_detect(pin,GPIO.RISING,callback=clean_cycle,bouncetime=300) # Setup event on pin 10 rising edge
    global pm
    pm.cycle()


def init_pins(pin):
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BCM) # Use number pin numbering
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

    serial = spi(port=0, address=0)
    return ssd1309(serial)

pages = make_page_list()
d = init_pins(button_pin)
pm = PageMachine(pages, device=d)
GPIO.add_event_detect(button_pin,GPIO.RISING,callback=clean_cycle,bouncetime=300) # Setup event on pin 10 rising edge
pm.cycle()