from django.db import models
from django.utils import timezone

from metaTest.managers import MetaTestManager

class MetaTest(models.Model):
    name=models.CharField(max_length=100,unique=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    objects=MetaTestManager()

    def __str__(self):
        return self.name