from re import T
import requests

user_input = input("Enter city: ")
print(user_input)
api_key = "831df29aaea9d75e516fb1d20e1b84ff"
weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No city found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = weather_data.json()['main']['temp']

    print(f"The weather in {user_input} are {weather}")
    print(f"The temperature in {user_input} is {temp}")