from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    completed = models.BooleanField(default=False)


