# IntM_django

API для интернет магазина, фронт на React https://github.com/SergeiTabinaev/IntM_react

Интернет магазин в возможностью создания через админку: категорий, товаров, характеристик и значений

Что еще в работе: 
  
     api для заказа товаров (Order)

Использованы следующие технологии: 

    Django REST framework,
    
    Авторизация и регистрация сделана с библиотекой djoser

Как использовать:

Клонировать репозиторий git clone ссылка_сгенерированная_в_вашем_репозитории

Создать виртуальное окружение python -m venv venv

Активировать виртуальное окружение

В settings.py прописать конект к БД. сделать миграции: manage.py makemigrations, manage.py migrate.

Cоздать суперпользователя: manage.py createsuperuser

Устанавливить зависимости: pip install -r reqs.txt

Запустить сервер python manage.py runserver

Открыть http://127.0.0.1:8000/swagger/
