from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Leaderboard
import random
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')


def game(request):
    return render(request, 'game.html')


def gameBegins(request):
    pName = request.POST.get('playerName', '')
    Movies = Movie.objects.values('movie_name')
    marray = []
    for item in Movies:
        marray.append(item)
    movie_list = json.dumps(marray)
    return render(request, 'gamebegins.html', {"movie_list": movie_list})