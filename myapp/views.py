from django.shortcuts import render
import requests
import datetime

def index(request):
    if 'city' in request.GET:
        city = request.GET['city']
    else:
        city = 'firenze'

    appid = '4ed281ab308066637167f15915dec07d'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': city, 'appid': appid, 'units': 'metric'}

    r = requests.get(url=URL, params=PARAMS)
    if r.status_code == 200:
        res = r.json()
        description = res['weather'][0]['description']
        icon = res['weather'][0]['icon']
        temp = res['main']['temp']
    else:
        description = "N/A"
        icon = "N/A"
        temp = "N/A"

    day = datetime.date.today()

    return render(request, 'weatherapp/index.html', {'description': description, 'icon': icon, 'temp': temp, 'day': day, 'city': city})
