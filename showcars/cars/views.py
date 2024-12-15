from .services import car
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return car.index(request)

@login_required(login_url='login')
def new_car(request):
    return car.new_car(request)

def car_view(request, username, car_id):
    return car.car_view(request, username, car_id)

@login_required(login_url='login')
def car_edit(request, username, car_id):
    return car.car_edit(request, username, car_id)

@login_required(login_url='login')
def car_delete(request, username, car_id):
    return car.delete_car(request, username, car_id)

@login_required(login_url='login')
def add_comment(request, username, car_id):
    return car.add_comment(request, username, car_id)