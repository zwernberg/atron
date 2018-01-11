from django.db import models
positions = (
    (0, 'QB'),
    (1, 'RB'),
    (2, 'WR'),
    (3, 'K'), 
    (4, 'TE'),
    )

season_status = (
    (0, 'Preseason'),
    (1, 'In Season'),
    (2, 'Season Over')
)

class Season(models.Model):
    year = models.IntegerField()
    status = models.IntegerField(choices=season_status)

    def __str__(self):
        return str(self.year)
    


# Create your models here.
class League(models.Model):
    season = models.ForeignKey(
        Season,
        related_name='leagues',
        on_delete=models.CASCADE
    )
    division = models.CharField(max_length = 50)
    league_id = models.CharField(max_length=150)
    size = models.IntegerField()

    def __str__(self):
        return self.division


class Note(models.Model):
    week = models.IntegerField()
    author = models.CharField(max_length=100)
    text = models.TextField()
    season = models.ForeignKey(
        Season,
        related_name='notes',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.author + ": week " + str(self.week)

class Team(models.Model):
    team_name = models.CharField(max_length=150)
    team_owner = models.CharField(max_length=150)
    league_id = models.CharField(max_length = 50)
    division = models.CharField(max_length=50)
    avatarUrl = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.team_name


class Player(models.Model):
    team = models.ForeignKey(
        Team, 
        related_name='players',
        on_delete=models.CASCADE
        )
    name = models.CharField(max_length=150)
    position = models.IntegerField(choices=positions)
    player_Id = models.CharField(max_length=150)
    starting = models.BooleanField(default=True)

    def __str__(self):
        return self.name