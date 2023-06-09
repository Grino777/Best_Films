# Generated by Django 4.2 on 2023-06-08 11:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("films_app", "0013_rename_movie_id_usermovies_movie_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="movie_slug",
            field=models.SlugField(default="", unique=True, verbose_name="SLUG"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="movie",
            name="category",
            field=models.ManyToManyField(
                to="films_app.category", verbose_name="Категории"
            ),
        ),
    ]
