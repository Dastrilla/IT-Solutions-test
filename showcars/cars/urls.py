from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.new_car, name="new_car"),
    path('<str:username>/<int:car_id>/', views.car_view, name="car"),
    path("<str:username>/<int:car_id>/edit", views.car_edit, name="car_edit"),
    path("<str:username>/<int:car_id>/delete", views.car_delete, name="car_delete"),
    path("<username>/<int:car_id>/comment", views.add_comment, name = "add_comment"),
]
