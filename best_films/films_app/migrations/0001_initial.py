# Generated by Django 4.2 on 2023-04-21 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, verbose_name='Категория')),
                ('slug', models.SlugField(blank=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=100, verbose_name='Название')),
                ('original_title', models.CharField(blank=True, default='', max_length=100, verbose_name='Оригинальное название')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='films_app.category', verbose_name='Жанр')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
        migrations.CreateModel(
            name='UserMovies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewing_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата просмотра')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='films_app.movie', verbose_name='Movie ID')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ID')),
                ('view_status', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='films_app.status', verbose_name='Статус просмотра')),
            ],
            options={
                'verbose_name_plural': 'Просмотры пользователей',
            },
        ),
    ]
