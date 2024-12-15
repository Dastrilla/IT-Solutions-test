
from cars.forms import CarForm, CommentForm
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from datetime import datetime as dt

from cars.models import Car, Comment
from cars.serializers import CarSerializer, CommentSerializer
from .permissions import IsAuthorOrREadOnly


User = get_user_model()

def index(request):
    car_list = Car.objects.order_by('-create_at').all()
    paginator = Paginator(car_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request,
                "index.html",
                {"page":page, 'paginator':paginator})

def new_car(request):
    context = {"title":"Новая публикация", "button":"Опубликовать"}
    form = CarForm(request.POST or None)
    if not form.is_valid() or  request.method != "POST":
        return render(request, "new_car.html", {"context":context, "form":form})
    car = form.save(commit=False)
    car.author = request.user
    car.save()
    
    return redirect("index")

def car_view(request, username, car_id):
    profile = get_object_or_404(User, username = username)
    car = get_object_or_404(Car, author__username = profile.username, id = car_id)
    cars = list(Car.objects
                .all()
                .select_related("author")
                .filter(author__username = profile.username)
                )
    
    form = CommentForm()
    items = car.comments.order_by('-created_at').all()

    return render(request, "car.html",
                  {"car": car,"profile": profile,
                    "form":form, "items":items})

def car_edit(request, username, car_id):
    context = {"title":"Редактирование записи", "button":"Сохранить"}
    car = get_object_or_404(Car, author__username = username, id = car_id)
    if request.user.username != car.author.username:
        return redirect("car", username=username, car_id = car_id)
    form = CarForm(request.POST or None, instance=car)
    if not form.is_valid() or request.method != "POST":
        return render(request, "new_car.html", {"context":context, "form":form, "car":car})
    form.save()
    car.update_at = dt.now()
    car.save()
    return redirect("car", username = username, car_id = car_id)

def delete_car(request, username, car_id):
    car = get_object_or_404(Car, author__username = username, id = car_id)
    if request.user.username != car.author.username:
        return redirect("car", username=username, car_id = car_id)
    Car.objects.filter(id = car_id).delete()
    return redirect("index")

def add_comment(request, username, car_id):
    car = get_object_or_404(Car, author__username = username, id = car_id)
    form = CommentForm(request.POST or None)
    if not form.is_valid() or request.method != "POST":
        return render(request, "comments.html", {"form":form, "car":car})
    comment = form.save(commit=False)
    comment.car = car
    comment.author = request.user
    comment.save()
    return redirect("car", username=username, car_id = car_id)

class CarAPIList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticatedOrReadOnly,)   

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)


class CarAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAuthorOrREadOnly,)


class CommentAPIList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)