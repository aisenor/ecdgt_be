from django.urls import path
from django.contrib import admin
from api.views import home

# from api.standings.list_view import StandingsAPIView
from api.contact.detail_view import ContactDetailView
from api.event.detail_view import EventDetailView
from api.event.list_view import EventListView
from api.event_results.detail_view import EventResultsDetailView
from api.event_results.list_view import EventResultsListView
from api.standings.list_view import StandingsListView
from api.division.detail_view import DivisionDetailView
from api.division.list_view import DivisionListView
from api.player.list_view import PlayerListView
from api.player.detail_view import PlayerDetailView


urlpatterns = [
    path('', home, name='home'),
    path('/', home, name='home'),
    path('admin/', admin.site.urls),

    path('contact/', ContactDetailView.as_view(), name="contact"),

    path('division/', DivisionListView.as_view(), name="division"),
    path('division/<pk>', DivisionDetailView.as_view(), name="division"),

    path('event/<pk>', EventDetailView.as_view(), name="event"),
    path('event/', EventListView.as_view(), name="event"),

    path('event_results/<pk>', EventResultsDetailView.as_view(), name="event_results"),
    path('event_results/', EventResultsListView.as_view(), name="event_results"),

    path('player/<pk>', PlayerDetailView.as_view(), name="player"),
    path('player/', PlayerListView.as_view(), name="player"),

    path('standings/', StandingsListView.as_view(), name="standings"),
]
