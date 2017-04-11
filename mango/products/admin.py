from django.contrib import admin
from models import Policy, CoverageType, CoverageDetail, Extras
# Register your models here.
admin.site.register(Policy)
admin.site.register(CoverageType)
admin.site.register(CoverageDetail)
admin.site.register(Extras)
