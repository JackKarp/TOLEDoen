import requests
import canvasapi

def read_envfile():
    dict = {}
    with open("./canvas/env") as envfile:
        for line in envfile:
            stripped_line = "".join(line.split()).split(":")
            dict[stripped_line[0]] = stripped_line[1] 
    return dict


envdict = read_envfile()
print(envdict)
res = requests.get(f"https://canvas.ubc.ca/api/v1/users/self", headers={"Authorization" : f"Bearer {envdict["apikey"]}"})
print(res)