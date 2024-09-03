from urllib.request import urlopen
import json

from luma.core.render import canvas
from sideways_text import wrapped_text

def read_envfile():
    dict = {}
    with open("./weather/env") as envfile:
        for line in envfile:
            stripped_line = "".join(line.split()).split(":", 1)
            dict[stripped_line[0]] = stripped_line[1] 
    return dict

def get_data():
    url = "https://api.weather.gov/points/" + read_envfile()["location"]
        
    # store the response of URL
    response = urlopen(url)

    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())

    # print the json response
    #print(data_json)

    #parse to forecast
    forecastlink = data_json['properties']['forecastHourly']

    #pull json from weather.gov
    fullforecast = urlopen(forecastlink)
    return json.loads(fullforecast.read())



def run_weather(device):
    data_forecast = get_data()
    next_forecast = data_forecast['properties']['periods'].pop(0)
    time = int(next_forecast["startTime"].split('T')[1].split(":")[0])
    if time > 12:
        time = time % 12
        time = str(time) + "pm"
    temp = str(next_forecast["temperature"]) + next_forecast["temperatureUnit"]
    rain = int(next_forecast["probabilityOfPrecipitation"]["value"])
    short = next_forecast["shortForecast"]
    string = f"Time:{time} \nTemp:{temp} \nDescription:{short}"
    # if rain > 30:
    #     string = string + f"Rain Chance: {rain}"
    # lines = wrapped_text(string)
    # lines = ': '.join(lines.split(':'))
    with canvas(device) as draw:
        draw.text((25, 3),time, fill="white",align='center',font_size=10)
        draw.text((0,20),temp, fill = "white",align='center',font_size=36)
        draw.text((20, 60),short, fill = "white",align='center',font_size=10)
        if rain > 30:
            draw.text((40, 70),rain + "%", fill = "white",align='center',font_size=10)
        # for i, line in enumerate(lines):
        #     draw.text((3, i*10),line, fill="white")


