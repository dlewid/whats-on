from django.shortcuts import render
from .models import Event

# Create your views here.

from django.http import HttpResponse

def index(request):
    event_list = Event.objects.all()
    context = {
        "events" : event_list,
    }
    return render(request, 'events/index.html', context)
