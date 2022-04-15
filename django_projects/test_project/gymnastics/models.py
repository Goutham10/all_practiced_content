from distutils.command.upload import upload

from django.db import models

# Create your models here.

class Trainers(models.Model):
    
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    email = models.EmailField()
