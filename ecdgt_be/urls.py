from django.urls import path
from django.contrib import admin
from api.views import home

# from api.standings.list_view import StandingsAPIView
from api.contact.detail_view import ContactDetailView
from api.tour_dates.detail_view import TourDatesDetailView
from api.tour_dates.list_view import TourDatesListView
from api.tour_standings.detail_view import TourStandingsDetailView
from api.tour_standings.list_view import TourStandingsListView
from api.division.detail_view import DivisionDetailView
from api.division.list_view import DivisionListView

urlpatterns = [
    path('', home, name='home'),
    path('/', home, name='home'),
    path('admin/', admin.site.urls),

    path('contact/', ContactDetailView.as_view(), name="contact"),
    path('tour_dates/', TourDatesListView.as_view(), name="tour_dates"),
    path('tour_dates/<pk>', TourDatesDetailView.as_view(), name="tour_dates"),
    path('tour_standings/', TourStandingsListView.as_view(), name="tour_standings"),
    path('tour_standings/<pk>', TourStandingsDetailView.as_view(), name="tour_standings"),
    path('division/', DivisionListView.as_view(), name="division"),
    path('division/<pk>', DivisionDetailView.as_view(), name="division"),

    # path("players/", PlayersListView.as_view(), name="players"),
    # path("players/<pk>", PlayersDetailView.as_view(), name="players"),
    #
    # path("putting_league/", PuttingLeagueListView.as_view(), name="putting_league"),
    # path("putting_league/<pk>", PuttingLeagueDetailView.as_view(), name="putting_league"),
    # path("putting_league/<int:player_id>", PuttingLeagueListView.as_view(), name="putting_league"),
    # path('standings/', StandingsAPIView.as_view(), name='standings'),
    # path('my_scores/', PuttingLeagueListView.as_view(), name="putting_league")
]
