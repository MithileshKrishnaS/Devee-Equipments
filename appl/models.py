import os
import random
from django.db import models
from dynamic_image.fields import DynamicImageField
# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    new_filename = random.randint(1, 123123123123)
    final_name = f"{new_filename}{ext}"
    return f"/{final_name}"

class product(models.Model):
    CATEGORY = (
        ('water pump controller','water pump controller'),
        ('level sensor','level sensor'),
        ('light master','light master'),
        ('gsm mobile starter','gsm mobile starter'),
        ('automatic starter','automatic starter'),
    )
    home = (
        ('yes','yes'),
        ('no','no'),
    )
    product_name = models.CharField(max_length=200,null=True)
    phase = models.CharField(max_length=200,null=True)
    voltage = models.CharField(max_length=200,null=True)
    frequency = models.CharField(max_length=200,null=True)
    usage = models.CharField(max_length=200,null=True)
    category = models.CharField(max_length=200,null=True,choices=CATEGORY)
    description = models.TextField(default='')
    add_to_home = models.CharField(max_length=200,null=True,choices=home)
    #image = DynamicImageField()
    image = models.ImageField(blank = True,default = 'default.png',null=True)

    
    def __str__(self):
        return self.product_name

class Customer(models.Model):
    
    name    = models.CharField(max_length=200,null=True)
    pno     = models.CharField(max_length=20,null=True)
    #product = models.OneToOneField(product,on_delete=models.CASCADE,blank=True,null=True)
    product = models.CharField(max_length=20,null=True)
    date     = models.DateTimeField(auto_now_add=True,null=True)
 
    def __str__(self):
        return self.name