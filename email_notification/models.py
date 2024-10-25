from django.db import models

from user.models import UserProfile


class Contact(models.Model):
    """
    Модель обратной связи
    """
    subject = models.CharField(max_length=255, verbose_name='Тема письма')
    email = models.EmailField(max_length=255, verbose_name='Электронный адрес (email)')
    content = models.TextField(verbose_name='Содержимое письма')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')
    profile = models.ForeignKey(UserProfile,
                             verbose_name='Пользователь',
                             on_delete=models.CASCADE,
                             )
    is_answered = models.BooleanField(verbose_name='Отвечено', default=False, blank=True)

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ['-created_at']


class EmailSubscription(models.Model):
    """Subscribed email to new posts."""
    email = models.EmailField('Email', unique=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = ('Email подписка(у)')
        verbose_name_plural = ('Email подписки')
