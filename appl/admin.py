from django.contrib import admin

# Register your models here.
from .models import *
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'pno', 'product')
    list_filter = ('date',)
    date_hierarchy = 'date' 
    ordering = ('date',)
    fields = ('name', 'pno', 'product') 

admin.site.register(product)
admin.site.register(Customer,CustomerAdmin)