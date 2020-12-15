from django.contrib import admin

# Register your models here.
from .models import Movie, Leaderboard

admin.site.register(Movie)
admin.site.register(Leaderboard)