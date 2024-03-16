import requests # Requires installation of requests library

r = requests.get('http://spartacodingclub.shop/en/global_air/seoul')
rjson = r.json()

days = rjson['data']['forecast']

for day in days:
		print(day['day'], day['avg'])