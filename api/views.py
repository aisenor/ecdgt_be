from django.http import JsonResponse


def home(request):
    data = {'message': 'Welcome to the future home of the East Coast Disc Golf Tour!'}
    return JsonResponse(data)
