import requests
import random

# Task 1
sites = ['google.com', 'facebook.com', 'twitter.com', 'amazon.com', 'apple.com']
random_site = random.choice(sites)
res = requests.get(f'https://{random_site}')
print(f'Status code: {res.status_code}, Site name: {random_site}, Length of HTML code: {len(res.text)}')

# Task 2
city_name = input('Please write name of the city: ')
geo_res = requests.get(f'https://geocoding-api.open-meteo.com/v1/search?name={city_name}')
geo_data = geo_res.json()
try:
    latitude = geo_data['results'][0]['latitude']
    longitude = geo_data['results'][0]['longitude']
except KeyError:
    print('Sorry but there is no such city')
else:
    query_params2 = {'latitude': latitude, 'longitude': longitude, 'current_weather': True}
    weather_res = requests.get('https://api.open-meteo.com/v1/forecast', params=query_params2)
    weather_data = weather_res.json()
    print(weather_data['current_weather'])
