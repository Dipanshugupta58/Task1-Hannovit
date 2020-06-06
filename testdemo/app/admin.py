from django.contrib import admin
from app.models import Record
# Register your models here.

class RecordAdmin(admin.ModelAdmin):
    list_display = ('id','name','pan','age','gender','email','city')


admin.site.register(Record,RecordAdmin)
