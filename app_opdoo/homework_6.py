import datetime as dt
import time
import requests
import json
from pathlib import Path

import urllib3

# print("###################################################################################")
# print("#     sw_vehicle_search(cargo_capacity: int, max_speed: int, cost: int) -> list   #")
# print("###################################################################################")

def sw_vehicle_search(cargo_capacity: int, max_speed: int, cost: int) -> list:

    current_page_url = "https://swapi.dev/api/vehicles/"
    source = requests.get(current_page_url).json()
    current_page_count = int(source['count'])

    final_vehicle_list = []

    if current_page_count == 0:
        final_vehicle_list = []
    else:
        while True:
            current_page_source = requests.get(current_page_url).json()
            page_vehicles_list = current_page_source["results"]
            for vehicle in page_vehicles_list:
                if vehicle["cargo_capacity"] != "unknown" and vehicle["cargo_capacity"] != "none" and vehicle["max_atmosphering_speed"] != "unknown" and vehicle["max_atmosphering_speed"] != "none" and vehicle["cost_in_credits"] != "unknown" and vehicle["cost_in_credits"] != "none":
                    cargo_capacity_test = int(vehicle["cargo_capacity"]) >= cargo_capacity if vehicle["cargo_capacity"] != 'unknown' else False
                    max_atmosphering_speed_test = int(vehicle["max_atmosphering_speed"]) >= max_speed
                    cost_in_credits_test = int(vehicle["cost_in_credits"]) <= cost if vehicle["cost_in_credits"] != 'unknown' else False

                    if cargo_capacity_test and max_atmosphering_speed_test and cost_in_credits_test:
                        final_vehicle_list.append(vehicle)

            current_page_next = current_page_source['next']
            if current_page_next is None:
                break
            else:
                current_page_url = current_page_next
                continue
    return final_vehicle_list

#print(sw_vehicle_search(755, 128, 252850))
# cargo_capacity = 755
# max_speed = 128
# cost = 252850
# The following vehicles meet this criteria:
# vehicle = ['C-9979 landing craft', 'Bantha-II cargo skiff']




# print("##############################################################")
# print("#     starship_piloted_species(starship_name: str) -> list   #")
# print("##############################################################")


def starship_piloted_species(starship_name: str) -> list:

    current_page_url = "https://swapi.dev/api/starships/"
    source = requests.get(current_page_url).json()
    current_page_count = int(source['count'])

    species_array = []

    if current_page_count == 0:
        species_array = []
    else:
        while True:
            current_page_source = requests.get(current_page_url).json()

            page_starship_list = current_page_source["results"]
            for starship in page_starship_list:
                if starship["name"] == starship_name:
                    pilot_urls = starship["pilots"]
                    if len(pilot_urls) == 0:
                       continue
                    else:
                        for pilot_url in pilot_urls:
                            pilot_source = requests.get(pilot_url).json()
                            specie_urls = pilot_source["species"]
                            if(len(specie_urls) == 0):
                                species_array.append("Human")
                            else:
                                for specie_url in specie_urls:
                                    specie_source = requests.get(specie_url).json()
                                    name = specie_source["name"]
                                    species_array.append(name)

            current_page_next = current_page_source['next']
            if current_page_next is None:
                break
            else:
                current_page_url = current_page_next
                continue

    return species_array

#print(starship_piloted_species('Death Star'))
#print(starship_piloted_species('Jedi starfighter'))


# print("###########################################")
# print("#     wear_a_jacket(us_zip:str) -> bool   #")
# print("###########################################")


def wear_a_jacket(us_zip: str) -> bool:

    lat = ""
    long = ""
    response = requests.get("https://gist.githubusercontent.com/erichurst/7882666/raw/5bdc46db47d9515269ab12ed6fb2850377fd869e/US%2520Zip%2520Codes%2520from%25202013%2520Government%2520Data")
    for line in response.iter_lines():
        line = line.decode("utf-8", "ignore") 
        line.replace(" ", "")

        if line.split(',')[0] == us_zip:
            lat = float(line.split(',')[1])
            long = float(line.split(',')[2])
    # print("lat",lat)
    # print("long",long)

    link = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=8b05661afa27c97147b938cd4c225bdf&units=imperial".format(
        lat, long)

    #url = end_point+"lat="+lat+"&lon="+long+"&appid="+api_key
    # print(link)
    source = requests.get(link).json()
    main_feels_like = int(source["main"]["feels_like"])
    weather_main = source["weather"][0]["main"]
    # print(main_feels_like)
    # print(weather_main)

    weather_mains_test = ('Rain', 'Snow')

    if main_feels_like <= 60 or weather_main in weather_mains_test:
        return True
    else:
        return False



# print("################################################################################")
# print("#     past_weather(days: int, hours: int, minutes: int, us_zip: str) -> bool   #")
# print("################################################################################")

import urllib.parse
def past_weather(days: int, hours: int, minutes: int, us_zip: str):

    oneday = dt.datetime.now() - dt.timedelta(days=days)
    oneday = oneday - dt.timedelta(hours=hours)
    oneday = oneday - dt.timedelta(minutes=minutes)
    date_time = oneday.strftime("%d/%m/%Y %H:%M")

    timestamp = int(dt.datetime.strptime(
        date_time, "%d/%m/%Y %H:%M").timestamp())

    lat = ""
    long = ""

    response = requests.get("https://gist.githubusercontent.com/erichurst/7882666/raw/5bdc46db47d9515269ab12ed6fb2850377fd869e/US%2520Zip%2520Codes%2520from%25202013%2520Government%2520Data")
    for line in response.iter_lines():
        line = line.decode("utf-8", "ignore") 
        line.replace(" ", "")
        if line.split(',')[0] == us_zip:
            lat = float(line.split(',')[1])
            long = float(line.split(',')[2])
    print(lat,"-",long)
    #62.402203,-146.945594
    link = "http://api.openweathermap.org/data/2.5/onecall/timemachine?lat={}&lon={}&dt={}&appid=8b05661afa27c97147b938cd4c225bdf&units=imperial".format(
        lat, long, timestamp)

    print(link)
    source = requests.get(link).json()

    return source["current"]["temp"]

#print("past_weather : ", past_weather(3, 8, 54,"99588"))
#Days = 3, Hours = 8, Minutes = 54, Zip = 99588


# print("#########################################################")
# print("#     cat_language(breed: str, language: str) -> bool   #")
# print("#########################################################")

def cat_language(breed: str, language: str) -> bool:

    cat_toket = "dc27af23-5b2e-4bd1-ad96-5872f218ed45"

    link = "https://api.thecatapi.com/v1/breeds"

    # print(link)
    source = requests.get(link).json()
    res = True

    for cat in source:
        if str(cat["name"]).lower() == str(breed).lower():
            country_code = cat["country_code"]
            link2 = "https://restcountries.com/v2/alpha/{}".format(
                country_code)
            source_2 = requests.get(link2).json()
            if language in source_2["languages"][0].values():
                res = True
            else:
                res = False
    return res


#print(cat_language('colorpoint shorthair', 'nn'))