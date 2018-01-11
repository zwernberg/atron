from django.urls import path
from week import views
app_name = 'week'

urlpatterns = [
    path('<int:week>/', views.matchups_view, name='matchup'),
]