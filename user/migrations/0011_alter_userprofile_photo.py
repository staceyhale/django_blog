# Generated by Django 5.0.1 on 2024-08-16 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_remove_userprofile_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, default='user/img/girl.jpg', upload_to='avatars/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]