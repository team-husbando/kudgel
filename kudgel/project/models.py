from django.db import models

from kudgel.user.models import User


class Project(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    staff = models.ManyToManyField(User, related_name='team', blank=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    title = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title
