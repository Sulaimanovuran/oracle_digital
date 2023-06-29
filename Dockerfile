#Скачиваем базовый образ
FROM python:3.9.5-slim

#Логгируем
ENV PYTHONUNBUFFERED 1

#Создаем локальную директорию
RUN mkdir -p /app

#Делаем ее рабочей директорией
WORKDIR /app

#https://luis-sena.medium.com/creating-the-perfect-python-dockerfile-51bdec41f1c8
COPY requirements.txt .

#Копируем все файлы в этк директорию
ADD . .

#https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/
RUN apt-get update && \
 apt-get install -y postgresql-server-dev-all gcc python3-dev musl-dev && \
 pip install -r requirements.txt && \
 adduser --disabled-password --no-create-home app

USER app

#CMD python manage.py runserver
CMD gunicorn --bind 0.0.0.0:8000 app.wsgi:application -k eventlet