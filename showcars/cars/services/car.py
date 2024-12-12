from cars.forms import CarForm
from django.shortcuts import render, redirect

def new_car(request):
    context = {"title":"Новая публикация", "button":"Опубликовать"}
    form = CarForm(request.POST or None)
    if not form.is_valid() or  request.method != "POST":
        return render(request, "new_car.html", {"context":context, "form":form})
    car = form.save(commit=False)
    car.author = request.user
    car.save()
    
    return redirect("index")