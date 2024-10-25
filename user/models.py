from django.contrib.auth.base_user import AbstractBaseUser
from django.urls import reverse

from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models


class CustomUser(AbstractUser):
    class Meta:
        verbose_name = 'Пользователь(я)'
        verbose_name_plural = 'Пользователи'
        db_table = "auth_user"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        UserProfile.objects.get_or_create(user_id=self.id)


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, unique=True)
    bio = models.TextField(max_length=50, blank=True, verbose_name='O себе')
    photo = models.ImageField(upload_to='avatars/%Y/%m/%d/', default='user/img/girl.jpg', blank=True,
                              verbose_name='Фото')
    birth_date = models.DateField(null=True, blank=True, verbose_name='День Рождение')

    def get_absolute_url(self):
        return reverse('user_profile', kwargs={'id': self.id})

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.user.username
