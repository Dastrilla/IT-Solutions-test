from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Car(models.Model):
    make = models.CharField(
        max_length=100,
        help_text="Марка автомобиля",
        verbose_name="Марка"
        )
    model = models.CharField(
        max_length=100,
        help_text= "Модель автомобиля",
        verbose_name="Модель"
        )
    year = models.CharField(
        max_length=4,
        verbose_name="Год",
        blank=True
        )
    description = models.TextField(
        help_text="Описание автомобиля",
        verbose_name="Описание",
        blank=True
        )
    create_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
        )
    update_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата обновления"
        )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="cars",
        verbose_name="Автор записи"
        )

    def __str__(self):
        return self.model
    
    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"

class Comment(models.Model):
    content = models.TextField(
        help_text="Напишите свой комментарий",
        verbose_name="Текст комментария"
        )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания комментария"
        )
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Машина"
        )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Автор записи"
        )
    
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"