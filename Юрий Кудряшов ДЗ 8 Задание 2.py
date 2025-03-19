import requests
import json 
print('Введите название города: ')
city = input()

weather_api = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=12750ae64c3bf382f8a397fc8ba8bcd4&units=metric')

weather_api = weather_api.json()

print(f"Temperature in {city}: {weather_api['main']['temp']}")
print(f"Weather: {weather_api['weather'][0]['description']}")
