from django.db import models


class School(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школа'

    def __str__(self):
        return self.name