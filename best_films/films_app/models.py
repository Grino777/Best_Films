from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Категория')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Movie(models.Model):
    movie_title = models.CharField(max_length=100, verbose_name='Название')
    original_title = models.CharField(max_length=100, blank=True, default='', verbose_name='Оригинальное название')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Жанр')

    def __str__(self):
        return self.movie_title

class Status(models.Model):
    status = models.CharField(max_length=20, verbose_name='Статус')

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
