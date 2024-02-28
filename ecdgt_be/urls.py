from django.urls import path
from django.contrib import admin
from api.views import home

# from api.standings.list_view import StandingsAPIView
from api.contact.detail_view import ContactDetailView
from api.tour_dates.detail_view import TourDatesDetailView
from api.tour_dates.list_view import TourDatesListView

urlpatterns = [
    path('', home, name='home'),
    path('/', home, name='home'),
    path('admin/', admin.site.urls),

    path('contact/', ContactDetailView.as_view(), name="contact"),
    path('tour_dates/', TourDatesListView.as_view(), name="tour_dates"),
    path('tour_dates/<pk>', TourDatesDetailView.as_view(), name="tour_dates"),

    # path("players/", PlayersListView.as_view(), name="players"),
    # path("players/<pk>", PlayersDetailView.as_view(), name="players"),
    #
    # path("putting_league/", PuttingLeagueListView.as_view(), name="putting_league"),
    # path("putting_league/<pk>", PuttingLeagueDetailView.as_view(), name="putting_league"),
    # path("putting_league/<int:player_id>", PuttingLeagueListView.as_view(), name="putting_league"),
    # path('standings/', StandingsAPIView.as_view(), name='standings'),
    # path('my_scores/', PuttingLeagueListView.as_view(), name="putting_league")
]
