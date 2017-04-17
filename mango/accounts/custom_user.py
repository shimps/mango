from django.contrib.auth.models import User
from django.db import models

class AccountType(models.Model):

    individual = models.BooleanField(default = False)
    company = models.BooleanField(default = False)
    insurance_provider = models.BooleanField(default = False)
    medical_institution = models.BooleanField(default = True)
    police_station = models.BooleanField(default = True)
    service_agent = models.BooleanField(default = True)

    user = models.OneToOneField(User, related_name = 'account_type')
