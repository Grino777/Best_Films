# Generated by Django 4.2 on 2023-04-21 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films_app', '0006_remove_movie_category_movie_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='url',
            field=models.URLField(blank=True, default='', verbose_name='Ссылка'),
        ),
    ]
