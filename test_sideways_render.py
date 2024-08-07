from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1309
from PIL import Image

serial = spi(port=0, address=0)
device = ssd1309(serial)

with canvas(device) as draw:
    s = "test"
    t = Image.new('L',(120, 50))
    draw.draw(t)
    draw.text((0,0),s,fill="white")

    t.rotate('90')