from luma.core.render import canvas

def clear_display(device):
    print("clearing")
    with canvas(device) as draw:
        draw.clear()