from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def see_all_rooms(request):
    return HttpResponse("see All Room!")


def see_one_room(request, room_id, room_name):
    return HttpResponse(f"see room with id:{room_id}")
