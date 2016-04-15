from django.db import models
from django.utils.encoding import smart_unicode
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=False)
    #phone = models.IntegerField(max_length=10,unique=True, validators=[RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='Invalid number')])
    phone = models.CharField(max_length = 10, null=True, blank=True)
    #timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    #updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.email)


    #code
#class user(models.Model):
 #   username=models.OneToOneField(User)
  #  password=models.CharField(max_length=100)

