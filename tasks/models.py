from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=255)
    grading_image = models.CharField(max_length=255)
    testing_image = models.CharField(max_length=255)
