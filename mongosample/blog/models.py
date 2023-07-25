from djongo import models


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.EmbeddedField(model_container=Blog)
    headline = models.CharField(max_length=255)

    # authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.headline
    
    # @property
    # def blog(self):
    #     # Return the Blog object using the blog_name and blog_tagline fields
    #     return Blog(name=self.blog_name, tagline=self.blog_tagline)