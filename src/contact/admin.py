from django.contrib import admin

# Register your models here.
from .models import Contact

class contactadmin(admin.ModelAdmin):
    class Meta:
        model = Contact

admin.site.register(Contact, contactadmin)