from luma.core.render import canvas

def wrapped_text(string, device, offset=0):
    words = string.split(' ')
    new_words = []
    for i, word in enumerate(words):
        if len(word) > 10:
            if len(word) > 20:
                new_words.append(word[0:11])
                # offset += 10
                new_words.append(word[11:21])
                # offset += 10
                new_words.append(word[21:-1])
            else:
                new_words.append(word[0:11])
                # offset += 10
                new_words.append(word[11:-1])
        else:
            new_words.append(word)
    return new_words #, offset
