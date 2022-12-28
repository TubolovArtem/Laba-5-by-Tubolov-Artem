import requests

from cfg import api_key_weather


def weather():
    s_city = input('Где вы хотите узнать погоду?\n'
                   '>>> ')
    weather_request = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={'q': s_city, 'type': 'like', 'units': 'metric', 'appid': api_key_weather}).json()
    if weather_request['cod'] == '200':
        if weather_request['count'] != 0:
            main_weather = weather_request['list'][0]['weather'][0]['main']
            temp = weather_request['list'][0]['main']['temp']
            pressure = weather_request['list'][0]['main']['pressure']
            humidity = weather_request['list'][0]['main']['humidity']
            print(f'Погода: {main_weather}\n'
                  f'Температура: {temp} °C\n'
                  f'Давление: {pressure} гПа\n'
                  f'Влажность: {humidity} %\n')
        else:
            print('Такого города не найдено\n')
    else:
        print('Такого города не найдено\n')
