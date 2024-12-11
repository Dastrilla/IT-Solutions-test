from django.shortcuts import render
from django.http import HttpResponse
from .models import Car

# Create your views here.
def index(request):
    latest = Car.objects.all()
    output = []
    for item in latest:
        output.append(item.model)
    return HttpResponse('\n'.join(output))