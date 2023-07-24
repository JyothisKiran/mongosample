from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='book')
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)