from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255)
    docker_image = models.CharField(max_length=255)
    description = models.TextField(null=True)