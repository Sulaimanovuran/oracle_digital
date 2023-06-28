from django.db import models


from school.models import School
from teacher.models import Teacher


class Group(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название класса')
    teacher = models.ForeignKey(Teacher,
                                on_delete=models.SET_NULL,
                                related_name='group',
                                null=True,
                                verbose_name='Классный руководитель')
    school = models.ForeignKey(School,
                               on_delete=models.CASCADE,
                               related_name='groups',
                               verbose_name='Школа')
    
    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'

    def __str__(self):
        return self.name