import requests # Requires installation of requests library

r = requests.get('http://spartacodingclub.shop/en/global_air/seoul')
rjson = r.json()

days = rjson['data']['forecast']

for day in days:
    if day['avg'] < 60:
        details = f"day avg= {day['avg']} day = {day['day']}"
        print(details)