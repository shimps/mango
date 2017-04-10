from django.db import models
from django.contrib.auth.models import User

# Create your models here.

client_title_choices = (('MR','Mr'),('MRS','Mrs'),('MS','Ms'))
marital_status_choices = (('S', 'Single'), ('M','Married'), ('D','Divorced'), ('W','Widowed'))
gender_choices = (('M','Male'),('F','Female'))
province_choices = (('COP','Copperbelt'),('LUS','Lusaka'),('CEN','Central'),('NWE','North Western'),
                    ('EAS','Eastern'),('LUA','Luapula'),('NOR','Northern'),('MUC','Muchinga'),('SOU','Southern'),
                    ('WES','Western'))
country_choices = (('ZM','Zambia'),)

class ClientAccount(models.Model):
    
    title = models.CharField(max_length = 3, choices = client_title_choices, blank = True, null = True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 2, choices = gender_choices)
    dob = models.DateField(null = True, blank = True)
    nrc = models.CharField(max_length = 20, null = True, blank = True)
    marital_status = models.CharField(max_length = 1, choices = marital_status_choices, blank = True, null = True)
    telephone = models.CharField(max_length = 20, null = True, blank = True)
    email = models.CharField(max_length = 100, null = True, blank = True)
    address = models.CharField(max_length = 200, null = True, blank = True)
    city = models.CharField(max_length = 50, null = True, blank = True)
    province = models.CharField(max_length = 3, choices = province_choices, null = True, blank = True)
    country = models.CharField(max_length = 2, choices = country_choices, default = 'ZM', null = True, blank = True)

    #mango id must be unique and start from 10000
    mango_id = models.IntegerField(default = 10000, unique = True, null = True, blank = True)
    
    user = models.OneToOneField(User, related_name = 'profile')

    def __unicode__(self):
        return self.first_name+" "+self.last_name
    
    def save(self, *args,**kwargs):
        #Create mango ID only if first time saving
        if self.pk is None:
            super(ClientAccount, self).save(*args, **kwargs)
            self.mango_id = 10000 + self.id
            self.save()
        else:
            super(ClientAccount, self).save(*args, **kwargs)



        
        
        
        

    
