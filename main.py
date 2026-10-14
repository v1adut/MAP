from dotenv import load_dotenv
import os

import requests

load_dotenv()

variabila = os.getenv("API_KEY")

url = "https://api.openweathermap.org/data/2.5/weather?"

raspuns = requests.get(url, params={'lat':46, 'lon':26, 'appid':variabila}).json()

print(variabila)
print(raspuns)