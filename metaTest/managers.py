from django.db import models

class MetaTestManager(models.Manager):
    def create_meta_test(self,name):
        if not name:
            raise ValueError('Name needed')
        
        contact=self.model(
            name=name
        )
        contact.save(using=self._db)
        return contact