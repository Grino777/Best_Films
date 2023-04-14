from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserNick(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name='ID')
    user_nick = models.CharField(max_length=50, verbose_name='Никнейм')

    def __str__(self):
        return self.user_nick

    class Meta:
        verbose_name_plural = 'Никнеймы'