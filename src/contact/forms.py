__author__ = 'HIRENDRA'

from django import forms
from django.contrib.auth.models import User
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        # provides an association between modelform and model
       model = Contact

class userform(forms.ModelForm):
   class Meta:
        model = User
