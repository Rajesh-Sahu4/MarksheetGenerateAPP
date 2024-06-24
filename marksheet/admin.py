from django.contrib import admin
from marksheet.models import *
# Register your models here.


class markAdmin(admin.ModelAdmin):
    list_display=('rollno','name')

admin.site.register(markupdate,markAdmin)