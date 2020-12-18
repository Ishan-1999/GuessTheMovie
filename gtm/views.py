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


def leaderboards(request):
    global pName
    if request.method == 'POST':
        points = request.POST.get('stored_point', '')

        record = Leaderboard(player_name=pName ,points=points)
        record.save()
    
    records = Leaderboard.objects.all()
    return render(request, 'leaderboards.html', {'records': records})


pName = ''


def gameBegins(request):
    global pName
    pName = request.POST.get('playerName', '')
    Movies = Movie.objects.values('movie_name')
    marray = []
    for item in Movies:
        marray.append(item)
    movie_list = json.dumps(marray)
    return render(request, 'gamebegins.html', {"movie_list": movie_list})