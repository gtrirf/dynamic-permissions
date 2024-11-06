from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.user.tools import API_ACTION_CHOICES
from django.utils.safestring import mark_safe


class APIAction(models.Model):
    api = models.CharField(max_length=100)
    action = models.CharField(max_length=50, choices=API_ACTION_CHOICES)
    action_name = models.CharField(max_length=255, null=True, blank=True,)

    def __str__(self):
        return f"{self.api}_{self.action}"


class Role(models.Model):
    role = models.CharField(max_length=100, unique=True)
    api_actions = models.ManyToManyField(APIAction)

    def __str__(self):
        return self.role


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='', null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    def photo_tag(self):
        if self.image:
            return mark_safe(
                f'<img src="{self.image.url}" width="300px" />'
            )
        return "No Image"

    photo_tag.short_description = "My uploaded photo"

