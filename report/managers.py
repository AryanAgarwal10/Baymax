from authentication.utils import isValidPhoneNumber
from django.db import models
from rest_framework import status


class ReportManager(models.Manager):
    def create_report(self,owner):
        # if not phone_number:
        #     raise ValueError('Phone number needed')
        # if not isValidPhoneNumber(phone_number):
        #     raise ValueError('Invalid phone number format')
        # if not name:
        #     raise ValueError('Name needed')
        
        report=self.model(
            owner=owner
        )
        report.save(using=self._db)
        return report
    # def last_submitted_report(self):
    #     request=self.context.get('request')
    #     report=self.model.objects.filter(owner=request.user).latest()
    #     if report:
    #         return report.submited
    #     else:
    #         return
            
