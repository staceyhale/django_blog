# Generated by Django 5.0.1 on 2024-01-26 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_userprofile_bio_alter_userprofile_birth_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
    ]
