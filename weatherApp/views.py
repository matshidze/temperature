import requests
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from weatherApp.models import Weather
from django.contrib import messages
from django.contrib.auth import authenticate , login, logout


def registerPage(request):

    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Successfully Registered your Username is : " + user )
            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)

def loginPage(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            get_weather()
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'registration/login.html', context)

def get_weather():

    api_key = "78a48dd1fcbd10234ee98f9c25a5bb93"


    #api_key = "3de49393e4baaf1d1a4a326034002890"
    city_id = "993800"
    url = "http://api.openweathermap.org/data/2.5/forecast"
    querystring = {"id": 993800, "appid": api_key }

    response = requests.request("GET", url, params=querystring)
    r = response.json()

    if r.get('list'):
        # iterate through weather list
        for i in r.get('list'):
            dt_txt = i.get('dt_txt')
            main = i.get('main')
            temp_min = main.get('temp_min')
            temp_max = main.get('temp_max')
            hdity = main.get('humidity')
            # generate date to be stored in db
            average = (temp_max/temp_min)
            data = {
                'date': dt_txt,
                'minimum_temperature': temp_min,
                'maximum_temperature': temp_max,
                'average_temperature': average,
                'humidity': hdity,
                'rain': None
            }
            print(data)
            # Store in database
            Weather.objects.create(data=data)

def d_views(request):
    weather_results = Weather.objects.filter().order_by('-id')[:5]
    data = {
        'weather_results': weather_results
    }
    return render(request, 'home.html', context= data)

