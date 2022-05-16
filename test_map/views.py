import json

from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    return render(request, "test_map/map.html")


def save_points(request):
    payload = json.loads(request.body)
    for point in payload.get("points"):
        print(point)
    return JsonResponse({})


def get_points(request):
    points = [
        {'lat': 127.0994768, 'long': 37.3599796},
        {'lat': 127.0994768, 'long': 37.3573189},
        {'lat': 127.10497, 'long': 37.3566708},
        {'lat': 127.1123085, 'long': 37.3566708},
        {'lat': 127.1104202, 'long': 37.3615487},
        {'lat': 127.1036396, 'long': 37.3616169},
    ]
    return JsonResponse({
        "points": points,
    })