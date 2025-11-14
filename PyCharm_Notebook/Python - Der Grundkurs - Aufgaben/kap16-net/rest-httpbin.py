#!/usr/bin/env python3
import requests
response = requests.get('https://httpbin.org/get?q=123')
# Text
print(response.content.decode('utf-8'))
# JSON
data = response.json()
print(data)
# Status Code
print("Status:", response.status_code)
# Put-Request und Antwort
print("-- Put --")
data = {'firstName': 'John', 'lastName': 'Doe'}
response = requests.put('https://httpbin.org/put', json=data)
print(response.json())
# Get-Request mit Basic Authentitation
print("-- Get mit Basic Authentitation --")
url = 'https://httpbin.org/basic-auth/maria/topsecret'
response = requests.get(url, auth=('maria', 'topsecret'))
print("Status-Code:", response.status_code)
