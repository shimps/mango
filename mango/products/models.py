from django.db import models
from accounts.models import InsuranceCompanyAccount
# Create your models here.

insurance_category_choices = (('H','Health'),('M','Motor'),('P','Property'),('T','Travel'),('C','Commercial'))
#insurance_subcategory_choices = (('G','General'),('V','Vision'),('D','Dental'))

#Basic structure of a policy
class Policy(models.Model):
    
    title = models.CharField(max_length = 200)
    category = models.CharField(max_length = 3, choices = insurance_category_choices)
    max_cover = models.FloatField(default = 0)
    coinsurance = models.IntegerField(default = 0)
    deductible = models.FloatField(default = 0)
    monthly_cost = models.FloatField(default = 0)
    
    insurance_company = models.ForeignKey(InsuranceCompanyAccount, related_name = 'policies', null = True, blank = True)

# A coverage category e.g. prescription drugs, hospital services
class CoverageType(models.Model):
    title = models.CharField(max_length = 200)
    policy = models.ForeignKey(Policy, related_name = 'coverage_types')

#Details e.g. hospital services -> xrays, outpatient surgeries etc
class CoverageDetail(models.Model):
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    coverage_type = models.ForeignKey(CoverageType, related_name = 'coverage_details')

#Make insurance cheaper by bundling to add coverage
class Extras(models.Model):
    monthly_cost = models.FloatField(default = 0)
    policy = models.ForeignKey(Policy, related_name = 'extras')
    
