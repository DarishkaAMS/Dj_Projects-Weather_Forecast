import requests
from django.shortcuts import render

# Create your views here.


def index(request):
    app_id = "7b06996e671b504dcc4a6e2ed52111ed"
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=' + app_id
    city = "London"

    response = requests.get(url.format(city))
    print(response.text)
    return render(request, 'weather/index.html')
