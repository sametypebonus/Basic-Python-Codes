import requests
api_key = "b4fcfaefd248446395b7f53309394e6d"
city = "Hyderabad"
url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key

request =requests.get(url)
json = request.json()
print(json)