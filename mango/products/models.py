from django.db import models
from accounts.models import InsuranceCompanyAccount, ClientAccount, CompanyAccount

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

    def __unicode__(self):
        return "%s - %s - %s"%(self.title, self.insurance_company.title, self.category)

# A coverage category e.g. prescription drugs, hospital services
class CoverageType(models.Model):
    
    title = models.CharField(max_length = 200)
    policy = models.ForeignKey(Policy, related_name = 'coverage_types')

    def __unicode__(self):
        return self.title

#Details e.g. hospital services -> xrays, outpatient surgeries etc
class CoverageDetail(models.Model):
    
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    
    coverage_type = models.ForeignKey(CoverageType, related_name = 'coverage_details')

    def __unicode__(self):
        return "%s - %s - %s"%(self.title,self.coverage_type.title,self.coverage_type.policy.title)

#Make insurance cheaper by bundling to add coverage
class Extras(models.Model):
    
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200, null = True, blank = True)
    monthly_cost = models.FloatField(default = 0)
    policy = models.ForeignKey(Policy, related_name = 'extras')

    def __unicode__(self):
        return "%s - %s - %s"%(self.title, self.policy.title, self.policy.insurance_company.title)

#Policy an individual has chosen    
class ClientPolicy(models.Model):
    
    policy = models.ForeignKey(Policy, related_name = 'client_policies')
    client = models.ForeignKey(ClientAccount, related_name = 'clients')
    active = models.BooleanField(default = False) # has user paid?
    cancelled = models.BooleanField(default = False) # has user cancelled?
    purchase_date = models.DateTimeField(auto_now_add = True)
    cancel_date = models.DateTimeField(null = True, blank = True)

#Policy a company/corporation has chosen
class CompanyPolicy(models.Model):

    policy = models.ForeignKey(Policy, related_name = 'company_policies')
    company = models.ForeignKey(CompanyAccount, related_name = 'companies')
    active = models.BooleanField(default = False) # has user paid?
    cancelled = models.BooleanField(default = False) # has user cancelled?
    purchase_date = models.DateTimeField(auto_now_add = True)
    cancel_date = models.DateTimeField(null = True, blank = True)
