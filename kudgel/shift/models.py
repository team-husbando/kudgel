from django.db import models
# from django.urls import reverse

from kudgel.user.models import User
from kudgel.project.models import Role
from kudgel.project.models import Project


class Shift(models.Model):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    name = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)

    all_day = models.BooleanField(default=False)
    date = models.DateField()
    start = models.TimeField(u'starting time', help_text='start time')
    end = models.TimeField(u'ending time', help_text='end time')

    def __str__(self):
        return self.name
