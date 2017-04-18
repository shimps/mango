from django.db import models
from django.contrib.auth.models import User
from time import time
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill,Transpose, SmartResize

#A Helper function to help with uploads.Generates a filename through a time string
def get_upload_file_name(instance,filename):
    return "uploads/profile_pictures/%s_%s"%(str(time()).replace('.','_'),filename)

# Create your models here.

client_title_choices = (('MR','Mr'),('MRS','Mrs'),('MS','Ms'))
marital_status_choices = (('S', 'Single'), ('M','Married'), ('D','Divorced'), ('W','Widowed'))
gender_choices = (('M','Male'),('F','Female'))
province_choices = (('COP','Copperbelt'),('LUS','Lusaka'),('CEN','Central'),('NWE','North Western'),
                    ('EAS','Eastern'),('LUA','Luapula'),('NOR','Northern'),('MUC','Muchinga'),('SOU','Southern'),
                    ('WES','Western'))
country_choices = (('ZM','Zambia'),)
employment_status_choices = (('E','Employed'),('U','Unemployed'),('S','Self Employed / Contractor'))


# clients are individual users
class ClientAccount(models.Model):
    
    title = models.CharField(max_length = 3, choices = client_title_choices, blank = True, null = True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    image = models.FileField(upload_to=get_upload_file_name,null=True,blank=True)
    image_thumbnail250= ImageSpecField(source='image',
                                       processors=[Transpose(),SmartResize(250,250)],
                                       format='JPEG',
                                       options={'quality':80})
    gender = models.CharField(max_length = 2, choices = gender_choices)
    dob = models.DateField(null = True, blank = True)
    nrc = models.CharField(max_length = 20, null = True, blank = True)
    employment_status = models.CharField(max_length = 2, choices = employment_status_choices, null = True, blank = True)
    marital_status = models.CharField(max_length = 1, choices = marital_status_choices, blank = True, null = True)
    telephone = models.CharField(max_length = 20, null = True, blank = True)
    email = models.CharField(max_length = 100, null = True, blank = True)
    address = models.CharField(max_length = 200, null = True, blank = True)
    city = models.CharField(max_length = 50, null = True, blank = True)
    pobox = models.CharField(max_length = 50, null = True, blank = True)
    province = models.CharField(max_length = 3, choices = province_choices, null = True, blank = True)
    country = models.CharField(max_length = 2, choices = country_choices, default = 'ZM', null = True, blank = True)

    #mango id must be unique and start from 10000
    mango_id = models.CharField(max_length = 20, default = 'p10000', unique = True, null = True, blank = True)
    
    user = models.OneToOneField(User, related_name = 'client_profile')

    def __unicode__(self):
        return self.first_name+' '+self.last_name
    
    def save(self, *args,**kwargs):
        #Create mango ID only if first time saving
        if self.pk is None:
            super(ClientAccount, self).save(*args, **kwargs)
            self.mango_id = 'p%s'%(10000 + self.id) # p stands for personal
            self.save()
        else:
            super(ClientAccount, self).save(*args, **kwargs)

#Corporate Accounts, will be able to but insurance and add/verify employees
class CompanyAccount(models.Model):

    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200,null = True, blank = True)
    image = models.FileField(upload_to=get_upload_file_name,null=True,blank=True)
    image_thumbnail250= ImageSpecField(source='image',
                                       processors=[Transpose(),SmartResize(250,250)],
                                       format='JPEG',
                                       options={'quality':80})
    telephone = models.CharField(max_length = 20, null = True, blank = True)
    email = models.CharField(max_length = 100, null = True, blank = True)
    address = models.CharField(max_length = 200, null = True, blank = True)
    city = models.CharField(max_length = 50, null = True, blank = True)
    pobox = models.CharField(max_length = 50, null = True, blank = True)
    province = models.CharField(max_length = 3, choices = province_choices, null = True, blank = True)
    country = models.CharField(max_length = 2, choices = country_choices, default = 'ZM', null = True, blank = True)

    #mango id must be unique and start from 10000
    mango_id = models.CharField(max_length = 20, default = 'c10000', unique = True, null = True, blank = True)
    user = models.OneToOneField(User, related_name = 'company_profile',null = True, blank = True)

    def __unicode__(self):
        return self.title
    
    def save(self, *args,**kwargs):
        #Create mango ID only if first time saving
        if self.pk is None:
            super(CompanyAccount, self).save(*args, **kwargs)
            self.mango_id = 'c%s'%(10000 + self.id) # c stands for company or corporate
            self.save()
        else:
            super(CompanyAccount, self).save(*args, **kwargs)

#Will be able to create policies and set prices
class InsuranceCompanyAccount(models.Model):

    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200,null = True, blank = True)
    image = models.FileField(upload_to=get_upload_file_name,null=True,blank=True)
    image_thumbnail250= ImageSpecField(source='image',
                                       processors=[Transpose(),SmartResize(250,250)],
                                       format='JPEG',
                                       options={'quality':80})
    telephone = models.CharField(max_length = 20, null = True, blank = True)
    email = models.CharField(max_length = 100, null = True, blank = True)
    address = models.CharField(max_length = 200, null = True, blank = True)
    city = models.CharField(max_length = 50, null = True, blank = True)
    pobox = models.CharField(max_length = 50, null = True, blank = True)
    province = models.CharField(max_length = 3, choices = province_choices, null = True, blank = True)
    country = models.CharField(max_length = 2, choices = country_choices, default = 'ZM', null = True, blank = True)
    
    user = models.OneToOneField(User, related_name = 'insurance_company_profile',null = True, blank = True)

    def __unicode__(self):
        return self.title
    
medical_service_choices = (('C','Clinic'),('H','Hospital'),('O','Other'))
#Hospitals, Clinincs, Private Practices etc
class MedicalAgentAccount(models.Model):

    title = models.CharField(max_length = 200)
    category = models.CharField(max_length = 1,choices = medical_service_choices, default = 'H')
    description = models.CharField(max_length = 200,null = True, blank = True)
    image = models.FileField(upload_to=get_upload_file_name,null=True,blank=True)
    image_thumbnail250= ImageSpecField(source='image',
                                       processors=[Transpose(),SmartResize(250,250)],
                                       format='JPEG',
                                       options={'quality':80})
    telephone = models.CharField(max_length = 20, null = True, blank = True)
    email = models.CharField(max_length = 100, null = True, blank = True)
    address = models.CharField(max_length = 200, null = True, blank = True)
    city = models.CharField(max_length = 50, null = True, blank = True)
    pobox = models.CharField(max_length = 50, null = True, blank = True)
    province = models.CharField(max_length = 3, choices = province_choices, null = True, blank = True)
    country = models.CharField(max_length = 2, choices = country_choices, default = 'ZM', null = True, blank = True)
    
    user = models.OneToOneField(User, related_name = 'medical_profile',null = True, blank = True)

    def __unicode__(self):
        return self.title

#Police Stations etc
class PoliceAgentAccount(models.Model):
    
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200,null = True, blank = True)
    image = models.FileField(upload_to=get_upload_file_name,null=True,blank=True)
    image_thumbnail250= ImageSpecField(source='image',
                                       processors=[Transpose(),SmartResize(250,250)],
                                       format='JPEG',
                                       options={'quality':80})
    telephone = models.CharField(max_length = 20, null = True, blank = True)
    email = models.CharField(max_length = 100, null = True, blank = True)
    address = models.CharField(max_length = 200, null = True, blank = True)
    city = models.CharField(max_length = 50, null = True, blank = True)
    pobox = models.CharField(max_length = 50, null = True, blank = True)
    province = models.CharField(max_length = 3, choices = province_choices, null = True, blank = True)
    country = models.CharField(max_length = 2, choices = country_choices, default = 'ZM', null = True, blank = True)
    
    user = models.OneToOneField(User, related_name = 'police_profile',null = True, blank = True)

    def __unicode__(self):
        return self.title

#General Service Agents e.g Garages
class ServiceAgentAccount(models.Model):

    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200,null = True, blank = True)
    image = models.FileField(upload_to=get_upload_file_name,null=True,blank=True)
    image_thumbnail250= ImageSpecField(source='image',
                                       processors=[Transpose(),SmartResize(250,250)],
                                       format='JPEG',
                                       options={'quality':80})
    telephone = models.CharField(max_length = 20, null = True, blank = True)
    email = models.CharField(max_length = 100, null = True, blank = True)
    address = models.CharField(max_length = 200, null = True, blank = True)
    city = models.CharField(max_length = 50, null = True, blank = True)
    pobox = models.CharField(max_length = 50, null = True, blank = True)
    province = models.CharField(max_length = 3, choices = province_choices, null = True, blank = True)
    country = models.CharField(max_length = 2, choices = country_choices, default = 'ZM', null = True, blank = True)

    user = models.OneToOneField(User, related_name = 'service_agent_profile',null = True, blank = True)

    def __unicode__(self):
        return self.title
    
agent_title_choices = (('MR','Mr'),('MRS','Mrs'),('MS','Ms'))
#People authorized by mango to handle mango business e.g. take payments, help on user behalf etc
class MangoAgent(models.Model):

    title = models.CharField(max_length = 3, choices = agent_title_choices, blank = True, null = True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    organization = models.CharField(max_length = 200, null = True, blank = True)
    image = models.FileField(upload_to=get_upload_file_name,null=True,blank=True)
    image_thumbnail250= ImageSpecField(source='image',
                                       processors=[Transpose(),SmartResize(250,250)],
                                       format='JPEG',
                                       options={'quality':80})
    gender = models.CharField(max_length = 2, choices = gender_choices)
    dob = models.DateField(null = True, blank = True)
    nrc = models.CharField(max_length = 20, null = True, blank = True)
    marital_status = models.CharField(max_length = 1, choices = marital_status_choices, blank = True, null = True)
    telephone = models.CharField(max_length = 20, null = True, blank = True)
    email = models.CharField(max_length = 100, null = True, blank = True)
    address = models.CharField(max_length = 200, null = True, blank = True)
    city = models.CharField(max_length = 50, null = True, blank = True)
    pobox = models.CharField(max_length = 50, null = True, blank = True)
    province = models.CharField(max_length = 3, choices = province_choices, null = True, blank = True)
    country = models.CharField(max_length = 2, choices = country_choices, default = 'ZM', null = True, blank = True)

    user = models.OneToOneField(User, related_name = 'mango_agent_profile')

    def __unicode__(self):
        return self.first_name+' '+self.last_name + ' - '+self.organization

    
class AccountType(models.Model):

    individual = models.BooleanField(default = False)
    company = models.BooleanField(default = False)
    insurance_provider = models.BooleanField(default = False)
    medical_institution = models.BooleanField(default = False)
    police_station = models.BooleanField(default = False)
    service_agent = models.BooleanField(default = False)

    user = models.OneToOneField(User, related_name = 'account_type')


        
        
        
        

    
