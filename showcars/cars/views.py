from django.shortcuts import render
from django.core.paginator import Paginator
from .services import car
from django.contrib.auth.decorators import login_required

from .models import Car

# Create your views here.
def index(request):
    car_list = Car.objects.order_by('-create_at').all()
    paginator = Paginator(car_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request,
                "index.html",
                {"page":page, 'paginator':paginator})

@login_required(login_url='login')
def new_car(request):
    return car.new_car(request)