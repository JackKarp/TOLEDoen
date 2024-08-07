from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1309
from PIL import Image, ImageDraw

serial = spi(port=0, address=0)
device = ssd1309(serial, rotate=3)

with canvas(device) as d:
    d.multiline_text((0,0),u"testing \n this thing",fill="white")

input()