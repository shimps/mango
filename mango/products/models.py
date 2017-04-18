from django.db import models
from accounts.models import InsuranceCompanyAccount, ClientAccount, CompanyAccount
from django.contrib.auth.models import User

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


title_choices = (('MR','Mr'),('MRS','Mrs'), ('MS','Ms'))
class Claim(models.Model):

    title = models.CharField(max_length = 3, choices = title_choices, null=True, blank = True)
    first_name = models.CharField(max_length = 50, blank = True, null = True)
    last_name = models.CharField(max_length = 50, null = True, blank = True)
    address = models.CharField(max_length = 200, null = True, blank = True)
    city = models.CharField(max_length = 50, null = True, blank = True)
    country = models.CharField(max_length = 50, null = True, blank = True)
    pobox = models.CharField(max_length = 50, null = True, blank = True)
    telephone = models.CharField(max_length = 50, null = True, blank = True)
    email_address = models.CharField(max_length = 100, null = True, blank = True)
    payment_method = models.CharField(max_length = 100, null = True, blank = True)
    payment_details = models.CharField(max_length = 100, null = True, blank = True)

    auto_insurance = models.BooleanField(default = False)

    policy = models.ForeignKey(ClientPolicy, related_name = 'policy_claims')
    user = models.ForeignKey(User, related_name = 'claims')

income_choices = (('L1K','< ZMW1000'),('B1K10K','ZMW 1000 - 10000'),('G1K','> ZMW 10000'))
funding_choices = (('S','Salary'),('B','Business'),('O','Other'))
class Application(models.Model):

    title = models.CharField(max_length = 3, choices = title_choices, null=True, blank = True)
    first_name = models.CharField(max_length = 50, blank = True, null = True)
    last_name = models.CharField(max_length = 50, null = True, blank = True)
    address = models.CharField(max_length = 200, null = True, blank = True)
    city = models.CharField(max_length = 50, null = True, blank = True)
    country = models.CharField(max_length = 50, null = True, blank = True)
    pobox = models.CharField(max_length = 50, null = True, blank = True)
    telephone = models.CharField(max_length = 50, null = True, blank = True)
    email_address = models.CharField(max_length = 100, null = True, blank = True)

    income = models.CharField(max_length = 10, choices = income_choices,null = True, blank = True)
    
    funding_sources = models.CharField(max_length = 3, choices = funding_choices, null = True, blank = True)
    funding_specify = models.CharField(max_length = 200, null = True, blank = True)

    auto_insurance = models.BooleanField(default = False)
    
    policy = models.ForeignKey(Policy, related_name = 'policy_applications')
    user = models.ForeignKey(User, related_name = 'policy_applications')


class AutoClaim(models.Model):

    registration_number = models.CharField(max_length = 100, null = True, blank = True)
    make = models.CharField(max_length = 100, null = True, blank = True)
    model = models.CharField(max_length = 100, null = True, blank = True)
    registration_date = models.DateField(null = True, blank = True)
    
    date_of_accident = models.DateField(null = True, blank = True)
    time_of_accident = models.CharField(max_length = 100, null = True, blank = True)
    place_of_accident = models.CharField(max_length = 100, null = True, blank = True)
    
    police_station = models.CharField(max_length = 100, null = True, blank = True)
    garage_name = models.CharField(max_length = 100, null = True, blank = True)
    loss_estimate = models.CharField(max_length = 100, null = True, blank = True)
    
    number_in_vehicle = models.CharField(max_length = 100, null = True, blank = True)
    name_of_driver = models.CharField(max_length = 100, null = True, blank = True) 
    dob_of_driver = models.DateField(null = True, blank = True)
    license_number = models.CharField(max_length = 100, null = True, blank = True)
    license_expiry_date = models.DateField(null = True, blank = True)
    vehicle_authorization = models.CharField(max_length = 200, null = True, blank = True)

    o_insurance_company = models.CharField(max_length = 200, null = True, blank = True)
    o_insurance_policy_number = models.CharField(max_length = 200, null = True, blank = True)
    o_insurance_start_date = models.DateField(null = True, blank = True)
    o_insurance_end_date = models.DateField(null = True, blank = True)

    claim = models.OneToOneField(Claim, related_name = 'auto_claim')
    

cover_choices = (('PKG','Package'),('FO','Fire Only'), ('TO','Theft Only'), ('LO','Liability Only'),
                 ('FT','Fire and Theft Only'),('FL','Fire and Liability Only'),('TL','Theft and Liability Only'))
vehicle_condition_choices = (('OO', 'Original Owner'),('SH','Second Hand'))
vehicle_usage_area_choices = (('U','Urban'),('R','Rural'))
vehicle_usage_type_choices = (('P','Private / Social'),('D','Driving Tuitions'), ('T','Towing'))


class AutoApplication(models.Model):
    
    type_of_cover = models.CharField(max_length = 3, choices = cover_choices, null = True, blank = True)
    vehicle_condition = models.CharField(max_length = 3, choices = vehicle_condition_choices, null = True, blank = True)
    make = models.CharField(max_length = 100,null = True, blank = True)
    model = models.CharField(max_length = 100, null = True, blank = True)
    seating_capacity = models.CharField(max_length = 3, null = True, blank = True)
    vehicle_usage_area = models.CharField(max_length = 3, choices = vehicle_usage_area_choices, null = True, blank = True)
    vehicle_usage_type = models.CharField(max_length = 3, choices = vehicle_usage_type_choices, null = True, blank = True)

    application = models.OneToOneField(Application, related_name = 'auto_application')
    
    
    
    
    
    
    
    
    
