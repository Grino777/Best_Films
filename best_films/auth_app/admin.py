from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(UserNick)
class UserNickAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user_nick']