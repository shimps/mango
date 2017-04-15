from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):

    sender = models.ForeignKey(User, related_name = 'sent_messages', null=True, blank = True)
    receiver = models.ForeignKey(User, related_name = 'received_messages', null=True, blank = True)
    subject = models.CharField(max_length = 200, null = True, blank = True)
    date_sent = models.DateTimeField(auto_now_add = True)
    body = models.CharField(max_length = 200)
