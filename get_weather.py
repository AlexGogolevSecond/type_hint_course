from requests import get
import json

loc = get('https://ipapi.co/json/').json()  # получаем текущие координаты по ip
latitude = loc.get('latitude')
longitude = loc.get('longitude')
current_coordinates = (latitude, longitude)
API_key = '12bbd44a983f8862cb28f02a47fe8444'

str_get_weather_api = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_key}'
raw_data_weather = json.loads(get(str_get_weather_api).text)
a = 0





