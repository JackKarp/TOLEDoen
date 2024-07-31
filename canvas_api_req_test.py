from canvasapi import Canvas

import button2



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
# print(envdict[api_url_string])

def get_content():
    canvas = Canvas(envdict[api_url_string], envdict[api_key_string])
    return canvas.get_courses()


button2.go(get_content()[0].name)