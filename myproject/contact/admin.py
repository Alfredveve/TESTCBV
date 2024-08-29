from django.contrib import admin
from . models import Contact



class AdminContact(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'message', 'created_at']
admin.site.register(Contact, AdminContact)
