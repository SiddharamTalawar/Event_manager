from django.contrib import admin
from .models import event

class eventAdmin(admin.ModelAdmin):
    list_display = ("event_name","discription","time","location")

admin.site.register(event, eventAdmin)    
