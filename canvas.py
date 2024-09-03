from canvasapi import Canvas
from luma.core.render import canvas
from sideways_text import wrapped_text

api_url_string = "apiurl"
api_key_string = "apikey"

# Reads an "env" file in the canvas folder into a dict. The env file should have "apikey" and "apiurl"
def read_envfile():
    dict = {}
    with open("./canvas/env") as envfile:
        for line in envfile:
            stripped_line = "".join(line.split()).split(":", 1)
            dict[stripped_line[0]] = stripped_line[1] 
    return dict

envdict = read_envfile()

def get_content():
    canvas = Canvas(envdict[api_url_string], envdict[api_key_string])
    return canvas.get_courses()

def run_canvas(device):
    content = get_content()
    lines = wrapped_text(content[1].name)
    with canvas(device) as draw:
        draw.text((3, i*10),lines, fill="white")
        # for i, line in enumerate(lines):
        #     draw.text((3, i*10),line, fill="white")
