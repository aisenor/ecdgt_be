import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

from backend.models.event import Event


class StandingsAPIView(APIView):
    def get(self, request):
        try:
            response = requests.get(f'{settings.API_URL}/event_results/')
            response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
            data = response.json()
            standings_data = process_data(data)
            return Response(standings_data, status=status.HTTP_200_OK)

        except requests.exceptions.RequestException as e:
            return Response(
                {"error": f"Failed to fetch data from other endpoint: {e}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


def process_data(data):
    tour_points = calc_tour_points(data["event_results"])
    return tour_points


def calc_tour_points(event_results):
    tour_points_by_division = {}

    for result in event_results:
        player_id = result["player"]
        event_points = int(result["event_points"])
        event_number = result["event"]
        division = result["division"]

        # Fetch event type from the Event model based on event number
        try:
            event_type = Event.objects.get(id=event_number).event_type_id
        except Event.DoesNotExist:
            # Handle case where event doesn't exist
            event_type = None

        if division not in tour_points_by_division:
            tour_points_by_division[division] = {}

        if player_id not in tour_points_by_division[division]:
            tour_points_by_division[division][player_id] = {
                "tour_points": 0,
                "event_type_1_points": [],
                "event_type_2_points": []
            }

        # Update points based on event type
        if event_type == 1:
            tour_points_by_division[division][player_id]["event_type_1_points"].append(event_points)
        elif event_type == 2:
            tour_points_by_division[division][player_id]["event_type_2_points"].append(event_points)

        for division, players in tour_points_by_division.items():
            for player_id, data in players.items():
                # Sort event points and take the best 5 for event type 2 and the best 1 for event type 1
                event_type_1_points = max(data["event_type_1_points"][:1]) if data["event_type_1_points"] else 0
                event_type_2_points = sum(sorted(data["event_type_2_points"], reverse=True)[:5])

                # Calculate total tour points for the player in the division
                total_points = event_type_1_points + event_type_2_points
                data["tour_points"] = total_points

    return tour_points_by_division
