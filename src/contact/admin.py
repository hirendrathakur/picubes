from django.contrib import admin

# Register your models here.
from .models import Contact

class contactadmin(admin.ModelAdmin):
        model = Contact
        search_fields = ['email']

admin.site.register(Contact, contactadmin)