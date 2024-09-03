from luma.core.render import canvas

def wrapped_text(string):
    words = string.split(' ')
    new_words = []
    for i, word in enumerate(words):
        if len(word) > 10:
            if len(word) >= 20:
                new_words.append(word[0:12])
                # offset += 10
                new_words.append(word[12:24])
                # offset += 10
                new_words.append(word[24:-0])
            else:
                new_words.append(word[0:12])
                # offset += 10
                new_words.append(word[12:-0])
        else:
            new_words.append(word)
    return "\n".join(new_words) #, offset
