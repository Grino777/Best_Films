# Generated by Django 4.2 on 2023-06-08 12:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("films_app", "0014_movie_movie_slug_alter_movie_category"),
    ]

    operations = [
        migrations.RenameField(
            model_name="category",
            old_name="slug",
            new_name="category_slug",
        ),
    ]