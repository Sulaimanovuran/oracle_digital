<center><h2>Система автоматизации школьных процессов</h2></center>

Все сделано максимально просто дабы повысить читабельность кода и возможность дальнейшего расширения проекта

* Запуск вручную с локального сервера
* Запуск с помощью docker-compose с web сервисом


<h3>Локальный запуск</h3>

Для безопасного запуска проекта на локальном сервере вашего устройства в ручную небходимо установить все зависимости внутри виртуального окружения.
Для это создайте аиртуальное окружение командой:

`python3 -m venv <Your virtualenv name>`

Затем активируйте окружение:

На Window:

`.\<Your virtualenv name>\Scripts\activate`

На linux $ macOS

`source venv/bin/activate`

Следующим шагом создание файла .env
В корневом каталоге вашего проекта создайте файл .env и запишите туда следующие переменные


"SC" Секретный ключ вашего проекта, вы можете его сгенерировать введя в терминале команду:

`python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`

Разрешенные хосты, если запускаете локально просто скопируйте код ниже:

`AH=localhost,127.0.0.1`

Название вашей базы данных его пользователя и пароль:

```
BN= Название Базы двнных
U= Имя пользователя
P= Пароль
```

Эл.почта и пароль от приложения для отправки электронных писем:

```
EMAIL_HOST_PASSWORD= Почта с которой отправляются сообщения
EMAIL_HOST_USER= Пароль для приложения (Зайдите в настройки аккаунта Google и в поиске наберите "Пароли приложений")
```


<h3>Запуск через docker-compose</h3>

