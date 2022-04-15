from statistics import mode
from django.db import models

class Student(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=30)
    dob = models.DateField()
    marks = models.IntegerField()
    email = models.EmailField()
    phonenumber = models.IntegerField()
    address = models.TextField()