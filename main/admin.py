from django.contrib import admin
from .models import People, Address

class MyModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'File')
    fields = ('id', 'File')

class MyModel(admin.ModelAdmin):
    list_display = ('id', 'City', 'Street')

# Register your models here.
admin.site.register(Address, MyModel)
admin.site.register(People, MyModelAdmin)