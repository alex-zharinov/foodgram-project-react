# Учебный проект в рамках курса "Python-разработчик" от ЯндексПрактикум. Спринт 14.
## Продуктовый помощник
## API-сервис для публикации отзывов на произведения, упакованный в контейнеры с помощью Docker
![workflow](https://github.com/alex-zharinov/foodgram-project-react/actions/.github/workflows/main.yml/badge.svg)
---
## Адрес сервера:

http://51.250.72.240/

## Документация проекта:
```
http://51.250.72.240/api/docs/
```

## Особенности:
- Cоздание рецептов, предустановленные ингредиетны и теги
- Пользовательские роли для управления и редактированием контентом.
- Подключена система подписок на авторов рецептов
- Добавление рецептов в изранное
- Корзина рецептов с возможностью скачать список продуктов для приготовления

## ⚙ Технологии
- _[Python 3.9](https://docs.python.org/3.9/)_
 - _[Django 3.2.16](https://docs.djangoproject.com/en/2.2/)_
 - _[Djoser 2.1.0](https://djoser.readthedocs.io/en/latest/)_
 -  _[Django REST framework](https://www.django-rest-framework.org/)_
- _[Request 2.26](https://pypi.org/project/requests/)_
---
### Запуск проекта в dev-режиме:

- Клонировать репозиторий и перейти в него в командной строке:

```bash
git git@github.com:alex-zharinov/foodgram-project-react.git
```

```bash
cd infra
```

- Запустите docker-compose:

```
docker-compose up
```

- Выполните по очереди команды:

```
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py collectstatic --no-input
docker-compose exec backend python manage.py load_ingredients_data
```

## ⤵️ Пример env-файла:
```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```

## ️ Автор - Жаринов Алексей
