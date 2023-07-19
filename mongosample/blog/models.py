from djongo import models

# Create your models here.


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField(max_length=150)

    class Meta:
        abstract = True


class Entry(models.Model):
    blog = models.EmbeddedField(model_container=Blog)