# Generated by Django 5.0.1 on 2024-01-23 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_userprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'Пользователь(я)', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
    ]
