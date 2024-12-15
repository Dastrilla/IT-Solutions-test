from django.urls import path, include
from . import views
from cars.services.car import *

urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.new_car, name="new_car"),
    path('<str:username>/<int:car_id>/', views.car_view, name="car"),
    path('<str:username>/<int:car_id>/edit', views.car_edit, name="car_edit"),
    path('<str:username>/<int:car_id>/delete', views.car_delete, name="car_delete"),
    path('<username>/<int:car_id>/comment', views.add_comment, name = "add_comment"),
    path('api/drf-auth/', include('rest_framework.urls')),
    path('api/cars/', CarAPIList.as_view()),
    path('api/cars/<int:pk>', CarAPIDetailView.as_view()),
    path('api/cars/<int:pk>/comments', CommentAPIView.as_view()),
]
