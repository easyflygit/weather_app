from django.db import models
from django.contrib.auth.models import User


class SearchHistory(models.Model):
    """Модель для сохранения истории поиска города и пользователя"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    search_count = models.IntegerField(default=0)
    last_searched = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.city}'

