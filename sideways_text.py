from luma.core.render import canvas

def wrapped_text(string):
    new_words = []
    for i in range(0, len(string), 10):
        new_words.append(string[i:i+10])
    # if len(string) > 10:
    #     if len(word) >= 20:
    #         new_words.append(word[0:12])
    #         # offset += 10
    #         new_words.append(word[12:24])
    #         # offset += 10
    #         new_words.append(word[24:len(word)])
    #     else:
    #         new_words.append(word[0:12])
    #         # offset += 10
    #         new_words.append(word[12:len(word)])
    # else:
    #     new_words.append(word)
    return "\n".join(new_words) #, offset
