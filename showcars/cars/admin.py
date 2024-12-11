from django.contrib import admin
from .models import Car, Comment
# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("make","model",
                    "year", "description", "author")

@admin.register(Comment) 
class ComentAdmin(admin.ModelAdmin):
    list_display = ("content","created_at", "car", "author")