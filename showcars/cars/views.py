from django.shortcuts import render
from django.http import HttpResponse
from .models import Car

# Create your views here.
def index(request):
    latest = Car.objects.all()
    return render(request, "index.html", {"cars":latest})