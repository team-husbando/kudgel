from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    title = models.CharField(max_length=50)

