from django.db import models

from kudgel.user.models import User
from kudgel.project.models import Role
from kudgel.project.models import Project


class Shift(models.Model):
    name = models.CharField(max_length=50, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.name
