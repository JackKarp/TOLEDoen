from canvasapi import Canvas
from luma.core.render import canvas

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
    with canvas(device) as draw:
        content = get_content()
        draw.text((0,0),content[0].name,fill="white")