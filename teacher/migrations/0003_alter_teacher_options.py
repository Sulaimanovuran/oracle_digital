# Generated by Django 4.2.2 on 2023-06-28 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_remove_teacher_activation_code_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Учителя', 'verbose_name_plural': 'Учителя'},
        ),
    ]
