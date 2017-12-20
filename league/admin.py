from django.contrib import admin
from league.models import Player, Team

# Register your models here.

class PlayerInline(admin.TabularInline):
    model = Player
    extra = 1


class TeamAdmin(admin.ModelAdmin):
    inlines = [
        PlayerInline,
    ]

class PlayerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)