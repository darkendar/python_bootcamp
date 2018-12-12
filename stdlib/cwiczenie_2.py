import json
from urllib.request import urlopen

# with urlopen("https://www.metaweather.com/api/location/search/?query=Warsaw") as file:
#     warszawa = json.loads(file.read().decode("utf-8"))
#
# print(warszawa)
# print(warszawa[0]["woeid"])
lokalizacja = input("Podaj miasto: ")
with urlopen(f"https://www.metaweather.com/api/location/search/?query={lokalizacja}") as file:
    miasto = json.loads(file.read().decode("utf-8"))

#print(miasto)

with urlopen(f"https://www.metaweather.com/api/location/{miasto[0]['woeid']}/") as file:
    dane = json.loads(file.read().decode("utf-8"))

prognozy = dane['consolidated_weather']
for prognoza in prognozy:
    print(f"Dzień: {prognoza['applicable_date']}")
    print(f"Max temperatura: {prognoza['max_temp']}")
    print(f"Cisnienie: {prognoza['air_pressure']} hPa")
    print(f"Wilgotność: {prognoza['humidity']}%")
    print()
