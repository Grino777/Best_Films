# Generated by Django 4.2 on 2023-04-26 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films_app', '0012_rename_category_id_usermovies_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermovies',
            old_name='movie_id',
            new_name='movie',
        ),
        migrations.RenameField(
            model_name='usermovies',
            old_name='user_id',
            new_name='user',
        ),
    ]