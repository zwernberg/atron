from django.contrib import admin
from league.models import Player, Team, League, Season, Note

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
    
class LeagueAdmin(admin.ModelAdmin):
    pass

class SeasonAdmin(admin.ModelAdmin):
    pass

class NotesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(League, LeagueAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Note, NotesAdmin)