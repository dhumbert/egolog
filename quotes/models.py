from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Quote(models.Model):
    user = models.ForeignKey(User)
    author = models.ForeignKey(Author)
    text = models.TextField()
    source = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=True)


