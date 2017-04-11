from django.contrib import admin
from models import ClientAccount, CompanyAccount, InsuranceCompanyAccount, ServiceAgentAccount, MedicalAgentAccount, PoliceAgentAccount, MangoAgent
# Register your models here.
admin.site.register(ClientAccount)
admin.site.register(CompanyAccount)
admin.site.register(ServiceAgentAccount)
admin.site.register(InsuranceCompanyAccount)
admin.site.register(PoliceAgentAccount)
admin.site.register(MedicalAgentAccount)
admin.site.register(MangoAgent)
