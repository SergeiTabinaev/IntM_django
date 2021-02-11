# IntM_django

API для интернет магазина, фронт на React https://github.com/SergeiTabinaev/IntM_react

Что еще в работе: 
  API для заказа товаров (Order)

Использованы следующие технологии: 
    Django REST framework
    Авторизация и регистрация сделана с библиотекой djoser

Как использовать:

Клонировать репозиторий git clone ссылка_сгенерированная_в_вашем_репозитории

Создать виртуальное окружение python -m venv venv

Активировать виртуальное окружение

В файле .env прописать конект к БД. сделать миграции: manage.py migrate, manage.py migrate.

Cоздать суперпользователя: manage.py createsuperuser

Устанавливить зависимости: pip install -r reqs.txt

Запустить сервер python manage.py runserver

Открыть http://127.0.0.1:8000/swagger/
