from django.db import models
from django.utils import timezone
from report.models import Report
from reportItem.managers import ReportItemManager

class TestName(models.TextChoices):
    MALE = 'MALE', 'MALE'
    FEMALE = 'FEMALE', 'FEMALE'
    OTHER = 'OTHER', 'OTHER'

class ReportItem(models.Model):
    report=models.ForeignKey(to=Report,on_delete=models.CASCADE)
    unit=models.CharField(max_length=20)
    value=models.BigIntegerField()
    test_name = models.CharField(max_length=20, choices=TestName.choices, default=TestName.MALE)
    active = models.BooleanField(default=True)
    submited=models.DateField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    objects=ReportItemManager()

    def __str__(self):
        return self.name