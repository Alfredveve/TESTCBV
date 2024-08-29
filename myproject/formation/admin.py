from django.contrib import admin
from . models import Formation



class AdminFormation(admin.ModelAdmin):
    list_display = ['title', 'description', 'certifier', 'price']

admin.site.register(Formation, AdminFormation)
