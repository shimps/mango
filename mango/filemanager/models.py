from django.db import models
from django.contrib.auth.models import User

#A Helper function to help with uploads.
def get_upload_file_name(instance,filename):
    return "uploads/files/%s"%(filename)

# Create your models here
class File(models.Model):

    filename = models.CharField(max_length = 200)
    upload_date = models.DateTimeField(auto_now_add = True)
    file_object = models.FileField(upload_to=get_upload_file_name, null = True, blank = True)

    user = models.ForeignKey(User, related_name = 'files')

    def __unicode__(self):
        return "%s uploaded: %s"%(filename,upload_date)
    
