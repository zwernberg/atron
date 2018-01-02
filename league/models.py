from django.db import models
positions = (
    (0, 'QB'),
    (1, 'RB'),
    (2, 'WR'),
    (3, 'K'), 
    (4, 'TE'),
    )

# Create your models here.
class League(models.Model):
    division = models.CharField(max_length = 50)
    league_id = models.CharField(max_length=150)

    def __str__(self):
        return self.division

class Team(models.Model):
    team_name = models.CharField(max_length=150)
    team_owner = models.CharField(max_length=150)
    league_id = models.CharField(max_length = 50)
    division = models.CharField(max_length=50)
    avatarUrl = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.team_name


class Player(models.Model):
    team = models.ForeignKey(Team, related_name='players')
    name = models.CharField(max_length=150)
    position = models.IntegerField(choices=positions, max_length=10)
    player_Id = models.CharField(max_length=150)
    starting = models.BooleanField(default=True)

    def __str__(self):
        return self.name