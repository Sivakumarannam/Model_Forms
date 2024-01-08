from django.contrib import admin

# Register your models here.
from app.models import *

class customizewebpage(admin.ModelAdmin):
    list_display=['topic_name','name','url','email']
    list_display_links=['topic_name','url']
    list_editable=['email','name']
    list_filter=['name','url','topic_name','email']
    list_per_page=1
    search_fields=['name']



admin.site.register(Topic)

admin.site.register(Webpage,customizewebpage)

admin.site.register(AccessRecords)


