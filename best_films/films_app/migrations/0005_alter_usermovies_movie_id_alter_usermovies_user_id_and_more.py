# Generated by Django 4.2 on 2023-04-13 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('films_app', '0004_usernick_usermovies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermovies',
            name='movie_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='films_app.movie', verbose_name='Movie ID'),
        ),
        migrations.AlterField(
            model_name='usermovies',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='usermovies',
            name='view_status',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='films_app.status', verbose_name='Статус просмотра'),
        ),
        migrations.AlterField(
            model_name='usermovies',
            name='viewing_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата просмотра'),
        ),
        migrations.AlterField(
            model_name='usernick',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ID'),
        ),
    ]
