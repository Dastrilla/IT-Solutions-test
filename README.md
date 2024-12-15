# Тестовое задание компании IT-Solutions: Создание веб-приложения для управления информацией об автомобилях с использованием API

Подробное ТЗ - https://drive.google.com/file/d/1RS2jPK6tdEJ1F01-mdydUzBGcRrrKwQA/view?usp=drive_link


Разработан по классической MVC архитектуре.

### Технологии
Python 3.12
Django 4.2
Django REST Framework
SQLite

Установка и настройка проекта
----------
1. Клонировать репозиторий:
```bash

git clone https://github.com/Dastrilla/IT-Solutions-test.git

```

2. Перейдите в директорию проекта для настройки, создайте и активируйте виртуальное окружение:
```bash
    cd IT-Solutions-test
    source venv/bin/activate
```

3. Установите зависимости из файла requirements.txt
```bush
    pip install -r requierments.txt
```

4. Выполните миграции:
```bash
 ./manage.py migrate
```

5. Запустить проект:
```bash
 ./manage.py runserver
```

Использование API
----------
API использует Session-based authentication

GET запросы:

Получение списка автомобилей  - http://127.0.0.1:8000/api/cars/
Получение информации о конткретном автомобили - http://127.0.0.1:8000/api/cars/<car_id>
Получение списка комментариев к автомобилю - http://127.0.0.1:8000/api/cars/<car_id>/comments

POST запросы:

Создание нового автомобиля - http://127.0.0.1:8000/api/cars/ - и передача в теле запроса [mark, model, year, description] в формате JSON
Создание нового комметария - http://127.0.0.1:8000/api/cars/<car_id>/comments - и передача в теле запроса [content] в формате JSON

PUT запросы:

Обновление данных об автомобиле - http://127.0.0.1:8000/api/cars/<car_id> - и передача в теле запроса обновленые данные [mark, model, year, description] в формате JSON

DELETE запросы:

Удаление автомобиля - http://127.0.0.1:8000/api/cars/<car_id>


На случай если не подгрузиться статика
----------
static в приложении cars - https://drive.google.com/file/d/1EEFYGt1bRHIHvsk_Nh5dwKBgR9UDImi1/view?usp=drive_link