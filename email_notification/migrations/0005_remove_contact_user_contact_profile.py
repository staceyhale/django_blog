# Generated by Django 5.0.1 on 2024-08-20 10:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_notification', '0004_alter_contact_user'),
        ('user', '0011_alter_userprofile_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
        migrations.AddField(
            model_name='contact',
            name='profile',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, to='user.userprofile', verbose_name='Пользователь'),
            preserve_default=False,
        ),
    ]