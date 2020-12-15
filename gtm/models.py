from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_id = models.AutoField
    movie_name = models.CharField(max_length=50)
    hint1 = models.CharField(max_length=50)
    hint2 = models.CharField(max_length=50)
    hint3 = models.CharField(max_length=50)

    def __str__(self):
        return self.movie_name


class Leaderboard(models.Model):
    player_id = models.AutoField
    player_name = models.CharField(max_length=50)
    points = models.IntegerField()

    def __str__(self):
        return self.player_name