from django.db import models
from kudgel.user.models import User


class Project(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Role(models.Model):
    title = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
