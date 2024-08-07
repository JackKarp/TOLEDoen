from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1309
from PIL import Image, ImageDraw

serial = spi(port=0, address=0)
device = ssd1309(serial)
img = Image.new('L', (120, 50))
img.rotate(90)
device.display(img)

input()