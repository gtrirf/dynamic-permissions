from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.user.tools import API_ACTION_CHOICES


class APIAction(models.Model):
    api = models.CharField(max_length=100)
    action = models.CharField(max_length=50, choices=API_ACTION_CHOICES)

    def __str__(self):
        return f"{self.api}_{self.action}"


class Role(models.Model):
    role = models.CharField(max_length=100, unique=True)
    api_actions = models.ManyToManyField(APIAction)

    def __str__(self):
        return self.role


class CustomUser(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)




