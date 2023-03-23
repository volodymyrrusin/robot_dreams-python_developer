import requests
import random

# Task 1
sites = ['google.com', 'facebook.com', 'twitter.com', 'amazon.com', 'apple.com']
random_site = random.choice(sites)
res = requests.get(f'https://{random_site}')
print(f'Status code: {res.status_code}, Site name: {random_site}, Length of HTML code: {len(res.text)}')

# Task 2
city_name = input('Please write name of the city: ')
res1 = requests.get(f'https://geocoding-api.open-meteo.com/v1/search?name={city_name}')
data1 = res1.json()
latitude = data1['results'][0]['latitude']
longitude = data1['results'][0]['longitude']

query_params2 = {'latitude': latitude, 'longitude': longitude, 'current_weather': True}
res2 = requests.get('https://api.open-meteo.com/v1/forecast', params=query_params2)
data2 = res2.json()
print(data2['current_weather'])