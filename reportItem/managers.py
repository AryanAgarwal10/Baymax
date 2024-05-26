from authentication.utils import isValidPhoneNumber
from django.db import models

class ReportItemManager(models.Manager):
    def create_report_item(self,report,value,test_name):
        # if not phone_number:
        #     raise ValueError('Phone number needed')
        # if not isValidPhoneNumber(phone_number):
        #     raise ValueError('Invalid phone number format')
        # if not name:
        #     raise ValueError('Name needed')
        
        reportItem=self.model(
            report=report,
            value=value,
            test_name=test_name
        )
        reportItem.save(using=self._db)
        return reportItem