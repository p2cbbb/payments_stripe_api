# Тестовое задание Django + Stripe API бэкенд
> Протестировать покупку товара можно по ссылке: https://payments-stripe-api.herokuapp.com/item/1/

### Задание:
##### Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
- Django Модель Item с полями (name, description, price) 
##### API с двумя методами:
- `GET /buy/{id}`, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item
- `GET /item/{id}`, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy

>Полный текст задания находится [по ссылке](https://github.com/p2cbbb/payments_api/blob/main/task.md)

### Копирование репозитория и установка зависимостей
```bash
git clone https://github.com/p2cbbb/payments_api
cd payments_api
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Устанавливаем переменные окружения
В папке `config` создать файл `.env` и заполнить eго ключами

```bash
SECRET_KEY=<secret_key>
STRIPE_PUBLIC_KEY=<stripe_public_key>
STRIPE_SECRET_KEY=<stripe_secret_key>
```
>Взять ключи `STRIPE_PUBLIC_KEY` и `STRIPE_SECRET_KEY` нужно [по ссылке](https://dashboard.stripe.com/login?redirect=%2Ftest%2Fapikeys)

### Применение миграций, создания суперпользователя и запуск проекта
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Разворачиваем проект через docker
```bash
docker-compose build
docker-compose up -d
docker-compose exec web pip install -r requirements.txt
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

