from django.db import models
from django.contrib.auth.models import User
from tasks.models import Task


class Submission(models.Model):
    task = models.ForeignKey(Task, related_name='submissions',
                             on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, related_name='submissions',
                             on_delete=models.SET_NULL)