from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1309
from PIL import Image, ImageDraw

serial = spi(port=0, address=0)
device = ssd1309(serial)

with canvas(device) as d:
    s = "test"
    d.text((0,0),s,fill="white")
    d._image.rotate('90')