from django.db import models
from authapp.models import User


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=64)
    link = models.URLField()
    users = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.name}'


class Todo(models.Model):
    pass
