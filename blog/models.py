from django.db import models
from django.urls import reverse

from user.models import UserProfile, CustomUser


class Tag(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(verbose_name='url', blank=True, unique=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse('tag', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(verbose_name='url', blank=True, unique=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse('category', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(verbose_name='url', blank=True, unique=True)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    views = models.IntegerField(verbose_name='Кол-во просмотров', default=0)
    created_at = models.DateTimeField(verbose_name='Опубликовано', auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    author = models.ForeignKey(UserProfile,
                               related_name="posts",
                               on_delete=models.CASCADE,
                               null=True, blank=True,
                               default='admin',
                               )
    
    def save(self, *args, **kwargs):
        x = super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse('post', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Статья(ю)'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']


class NetworkModel(models.Model):
    title = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100)
    url = models.URLField(max_length=200)

    class Meta:
        verbose_name = 'Социальная(ую) сеть'
        verbose_name_plural = 'Социальные сети'



