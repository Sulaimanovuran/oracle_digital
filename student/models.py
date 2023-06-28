from django.db import models


from group.models import Group

'''
ФИО
Mail
Дата рождения
Класс
Адрес
Пол
Фото(необязательно)

'''
class Student(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='Ф.И.О')
    email = models.EmailField(max_length=100, unique=True, verbose_name='Эл.почта')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    group = models.ForeignKey(Group,
                              on_delete=models.CASCADE,
                              related_name='students',
                              verbose_name='Класс')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    gender = models.CharField(max_length=10, verbose_name='Пол')
    picture = models.ImageField(upload_to='student_images/')

    class Meta:
        verbose_name = 'Ученик(ца)'
        verbose_name_plural = 'Ученики(цы)'


    def __str__(self) -> str:
        return self.email
    