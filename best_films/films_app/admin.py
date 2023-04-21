from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    prepopulated_fields = {'slug': ('category_name',)}

    def __str__(self):
        return 'Категории'

    class Meta:
        verbose_name = 'Категории'

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_title', 'original_title', 'description', 'url', 'category')

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('status',)


@admin.register(UserMovies)
class UserMoviesAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'movie_id', 'view_status', 'viewing_date')


