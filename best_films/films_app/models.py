from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Категория')
    category_slug = models.SlugField(db_index=True, verbose_name='URL')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Movie(models.Model):
    movie_title = models.CharField(max_length=100, verbose_name='Название')
    original_title = models.CharField(max_length=100, blank=True, default='', verbose_name='Оригинальное название')
    description = models.TextField(verbose_name='Описание', blank=True, default='')
    url = models.URLField(blank=True, default='', verbose_name='Ссылка')
    category = models.ManyToManyField(Category, verbose_name='Категории')
    movie_slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='SLUG')

    def __str__(self):
        return self.movie_title

    def get_category(self):
        return self.category


class Status(models.Model):
    status = models.CharField(max_length=20, verbose_name='Статус')

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class UserMovies(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, verbose_name='Название фильма')
    view_status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name='Статус просмотра')
    viewing_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата просмотра')
    category = models.ManyToManyField(Category, db_index=True, verbose_name='Категории')

    def __str__(self):
        return f'{self.user} - {self.movie}'

    def __hash__(self):
        return hash((self.user, self.movie, self.view_status, self.category))

    class Meta:
        verbose_name_plural = 'Просмотры пользователей'
