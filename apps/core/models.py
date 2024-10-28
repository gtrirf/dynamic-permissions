from django.db import models
from apps.user.models import CustomUser


class Group(models.Model):
    name = models.CharField(max_length=255)
    classroom = models.CharField(max_length=100)
    teacher = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='teacher_groups'
    )
    students = models.ManyToManyField(CustomUser, related_name='student_groups')

    def __str__(self):
        return self.name


class Events(models.Model):
    event_name = models.CharField(max_length=100)
    event_date = models.DateField()

    def __str__(self):
        return self.event_name

