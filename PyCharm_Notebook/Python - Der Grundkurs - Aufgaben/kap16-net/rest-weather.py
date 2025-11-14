#!/usr/bin/env python3
import requests

# Bitte besorgen Sie sich einen eigenen API-Schlüssel
# unter https://www.weatherapi.com/
# (kostenlos bei eingschränkter Nutzung des Dienstes)
key = "7901161c6b4e4806b4651739230304"
city = "Graz"
base = "https://api.weatherapi.com/v1/current.json"
url = "%s?key=%s&q=%s&aqi=no" % (base, key, city)
# print(url)
response = requests.get(url)
# print(response.content.decode('utf-8'))
data = response.json()
condition = data['current']['condition']['text']
print("Das Wetter in %s: %s" % (city, condition))
print("Temperatur:", data['current']['temp_c'], "°C")
