# Generated by Django 4.2 on 2023-04-13 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='category_id',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=50, verbose_name='Категория'),
        ),
    ]