from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Категория')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Movie(models.Model):
    movie_title = models.CharField(max_length=100, verbose_name='Название')
    original_title = models.CharField(max_length=100, blank=True, default='', verbose_name='Оригинальное название')
    description = models.TextField(verbose_name='Описание')
    url = models.URLField(verbose_name='Ссылка')
    category = models.ForeignKey(Category, db_index=True, on_delete=models.PROTECT, verbose_name='Жанр')

    def __str__(self):
        return self.movie_title

class Status(models.Model):
    status = models.CharField(max_length=20, verbose_name='Статус')

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class UserMovies(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name='ID')
    movie_id = models.ForeignKey(Movie, on_delete=models.PROTECT, verbose_name='Movie ID')
    view_status = models.ForeignKey(Status, on_delete=models.PROTECT, default='', verbose_name='Статус просмотра')
    viewing_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата просмотра')

    def __str__(self):
        return f'{self.user_id} - {self.movie_id}'

    class Meta:
        verbose_name_plural = 'Просмотры пользователей'