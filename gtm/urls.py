from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game' , views.game, name='game'),
    path('gamebegins' , views.gameBegins, name='gamebegins'),
    path('leaderboards' , views.leaderboards, name='leaderboards'),
]