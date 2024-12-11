from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Car(models.Model):
    make = models.CharField(max_length=100, help_text="Марка автомобиля", verbose_name="Марка")
    model = models.CharField(max_length=100, help_text= "Модель автомобиля", verbose_name="Модель")
    year = models.IntegerField(verbose_name="Год")
    description = models.TextField(help_text="Описание автомобиля", verbose_name="Описание")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    update_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата обновления")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cars", verbose_name="Автор записи")

    def __str__(self):
        return self.model