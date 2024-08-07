from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1309
from PIL import Image, ImageDraw

import textwrap

serial = spi(port=0, address=0)
device = ssd1309(serial, rotate=3)

"TODO: Figure out programatically how to wrap"
with canvas(device) as d:
    xy = (device.width, device.height)
    text = "testing this thingymajigy"
    wrapped = textwrap.wrap(text, width=11)
    d.multiline_text((0,0),'\n'.join(wrapped),fill="white")