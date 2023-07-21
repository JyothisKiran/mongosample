from djongo import models 
from django import forms

# Create your models here.


class Blog(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=50)
    plot = models.TextField(max_length=200)

    class Meta:
        abstract = True


class Entry(models.Model):
    blog = models.EmbeddedField(model_container=Blog)
    author = models.CharField(max_length=100)
    objects = models.DjongoManager()

    def __str__(self) -> str:
        return self.blog.name
