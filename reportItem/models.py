from django.db import models
from django.utils import timezone
from report.models import Report
from reportItem.managers import ReportItemManager

class TestName(models.TextChoices):
    MCV = 'MCV', 'MCV'
    RBC_Count = 'RBC Count', 'RBC Count'
    Sodium = 'Sodium', 'Sodium'
    Glucose_Fasting = 'Glucose Fasting', 'Glucose Fasting'
    Vitamin_B12 = 'Vitamin B12', 'Vitamin B12'
    T3 = 'T3', 'T3'
    T4 = 'T4', 'T4'
    TSH = 'TSH', 'TSH'
    Neutrophils = 'Neutrophils', 'Neutrophils'
    Lymphocyte = 'Lymphocyte', 'Lymphocyte'
    Monocytes = 'Monocytes', 'Monocytes'
    MCH = 'MCH', 'MCH'
    Hemoglobin = 'Hemoglobin', 'Hemoglobin'
    Platelet_Count = 'Platelet Count', 'Platelet Count'
    Mean_Platelet_Volume = 'Mean Platelet Volume', 'Mean Platelet Volume'
    Vitamin_D = 'Vitamin D', 'Vitamin D'
    HDL = 'HDL', 'HDL'
    LDL = 'LDL', 'LDL'
    Potassium = 'Potassium', 'Potassium'
    Chloride = 'Chloride', 'Chloride'

class ReportItem(models.Model):
    report=models.ForeignKey(to=Report,on_delete=models.CASCADE)
    value=models.BigIntegerField()
    test_name = models.CharField(max_length=20, choices=TestName.choices, default=TestName.MCV)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    objects=ReportItemManager()

    def __str__(self):
        return self.name