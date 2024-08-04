from luma.core.render import canvas

def clear_display(device):
    with canvas(device) as draw:
        draw.rectangle((0,0), fill=(0, 0, 0, 0))