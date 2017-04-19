from django.contrib import admin
from models import Policy, Claim, Application, AutoClaim, AutoApplication, CoverageType, CoverageDetail, Extras, ClientPolicy, CompanyPolicy
# Register your models here.
admin.site.register(Policy)
admin.site.register(Claim)
admin.site.register(Application)
admin.site.register(AutoClaim)
admin.site.register(AutoApplication)
admin.site.register(CoverageType)
admin.site.register(CoverageDetail)
admin.site.register(Extras)
admin.site.register(ClientPolicy)
admin.site.register(CompanyPolicy)
