from canvasapi import Canvas
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.oled.device import ssd1309
import asyncio

api_url_string = "apiurl"
api_key_string = "apikey"

CONTENT_MARGIN = 20
LINE_MARGIN = 4
FONT_SIZE = 10

# Reads an "env" file in the canvas folder into a dict. The env file should have "apikey" and "apiurl"
def read_envfile():
    dict = {}
    with open("./canvas/env") as envfile:
        for line in envfile:
            stripped_line = "".join(line.split()).split(":", 1)
            dict[stripped_line[0]] = stripped_line[1] 
    return dict

async def get_content():
    envdict = read_envfile()
    canvas = Canvas(envdict[api_url_string], envdict[api_key_string])
    state = await {"content" : canvas.get_courses()}
    return state

def render_canvas_no_scroll(device: ssd1309, state: dict):
    "Deprecated"
    content = state["content"]
    content_height = len(state["content"]) * (LINE_MARGIN + FONT_SIZE)
    if content_height + LINE_MARGIN <= device.height:
         with canvas(device) as draw:
              draw.multiline_text(text="\n".join(i.name for i in content), spacing=LINE_MARGIN, font_size=FONT_SIZE)
    else:
        raise Exception

def render_content(device: ssd1309, state: dict):
    content = state["content"]
    content_height = len(state["content"]) * (LINE_MARGIN + FONT_SIZE)
    virtual = viewport(device, width=device.width, height=content_height + LINE_MARGIN)
    with canvas(virtual) as draw:
            draw.multiline_text(text="\n".join(i.name for i in content), spacing=LINE_MARGIN, font_size=FONT_SIZE)

def scroll_content(virtual: viewport):
     for y in range(virtual.height):
          virtual.set_position(0, y)
          asyncio.sleep