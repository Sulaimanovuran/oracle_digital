from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUserManager(BaseUserManager):

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("The given username must be set")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
       
        user.save(using=self._db)
        return user

    def create_user(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, password, username, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, password, **extra_fields)


class Teacher(AbstractUser):

    full_name = models.CharField(max_length=100, verbose_name='Ф.И.О')
    username = models.CharField(max_length=50, unique=True, verbose_name='Имя пользователя')
    password = models.CharField(max_length=100, verbose_name='Пароль')
    phone = models.CharField(max_length=20, help_text='+996(707)-123-456', verbose_name='Тел.')
    subject = models.CharField(max_length=100, verbose_name='Предмет')
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name']

    objects = MyUserManager()


    class Meta:
        verbose_name = 'Учителя'
        verbose_name_plural = 'Учителя'
