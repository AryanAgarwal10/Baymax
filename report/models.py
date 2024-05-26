from django.db import models
from django.utils import timezone

from authentication.models import User
from .managers import ReportManager


class Report(models.Model):
    owner=models.ForeignKey(to=User,on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    submited=models.DateField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    objects=ReportManager()

    def __str__(self):
        return self.submited