from django.db import models
from django.utils import timezone

from authapp.models import User


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=64)
    link = models.URLField()
    users = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.name}'


class Todo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(editable=False)
    update_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.project} {self.text[:10]} {self.update_date} {self.user}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.create_date = timezone.now()
        self.update_date = timezone.now()
        return super().save(*args, **kwargs)
