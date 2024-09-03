from urllib.request import urlopen
import json

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
    time = int(next_forecast["startTime"].split('T')[1].split(":")[0]) % 12
    temp = str(next_forecast["temperature"]) + next_forecast["temperatureUnit"]
    rain = int(next_forecast["probabilityOfPrecipitation"]["value"])
    short = next_forecast["shortForecast"]

    offset = 0
    offset = wrapped_text(f"Time: {time}", device, offset)
    offset = wrapped_text(f"Temperature: {temp}", device, offset)
    if rain > 30:
        offset = wrapped_text(f"Rain Chance: {rain}", device, offset)
    offset = wrapped_text(f"Description: {short}", device, offset)


