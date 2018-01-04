"""atron URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from atron import settings
from league import views
from rest_framework.routers import DefaultRouter
from messaging.views import MessageViewSet

router = DefaultRouter()
router.register(r'api/messages', MessageViewSet, base_name='message')


urlpatterns = [
    url(r'^api/league/$', views.league_settings),
    url(r'^api/scoreboard/$', views.scoreboard_view),
    url(r'^api/championship/$', views.championship_view),
    url(r'^api/standings/$', views.standings_view),
    url(r'^api/teams/$', views.team_view),
    url(r'^api/admin/', admin.site.urls),
]
urlpatterns += router.urls

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
