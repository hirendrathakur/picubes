from django.db import models
from django.utils.encoding import smart_unicode
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=False)
    phone = models.CharField(max_length=10, null=True, blank=False)
    message = models.CharField(max_length = 1000, null=True, blank=True, unique=False)

    def __unicode__(self):
        return smart_unicode(self.email)


