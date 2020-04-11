import requests
import json

# url = 'https://www.cbr-xml-daily.ru/daily_json.js'
url = 'https://api.weather.yandex.ru/v1/informers?lat=55.75396&lon=37.620393'
response = requests.get(url)
data = json.loads(response.text)
print(data)