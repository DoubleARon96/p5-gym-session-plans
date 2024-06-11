from django.db import models
from django.contrib.auth.models import User


class HomeNews(models.Model):
    title = models.TextField(max_length=30,)
    content = models.TextField(max_length=2000)
    updated_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title