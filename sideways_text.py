from luma.core.render import canvas

def wrapped_text(string, device):
    words = string.split(' ')
    offset = 0
    with canvas(device) as draw:
        for i, word in enumerate(words):
            if len(word) > 10:
                if len(word) > 20:
                    draw.text((0,10*i + offset),word[0:11],fill="white")
                    offset += 10
                    draw.text((0,10*i + offset),word[11:21],fill="white")
                    offset += 10
                    draw.text((0,10*i + offset),word[21:-1],fill="white")
                else:
                    draw.text((0,10*i + offset),word[0:11],fill="white")
                    offset += 10
                    draw.text((0,10*i + offset),word[11:-1],fill="white")
            else:
                draw.text((0,10*i + offset),word,fill="white")
