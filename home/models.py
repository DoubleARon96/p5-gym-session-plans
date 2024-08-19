from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class HomeNews(models.Model):
    '''
    This will create the home news model
    '''
    title = models.TextField(max_length=100,)
    content = models.TextField(max_length=2000)
    updated_on = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)

    def __str__(self):
        return self.title
