from sqlite3 import Date
from unicodedata import category
from django.db import models
from django.forms import DateField

class Supermarket(models.Model):
    order_id = models.CharField(max_length=30)
    order_date = models.DateField()
    ship_date = models.DateField()
    ship_mode = models.CharField(max_length=30)
    customer_id = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=50)
    segment = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=30)
    postal_code = models.IntegerField()
    region = models.CharField(max_length=30)
    product_id = models.CharField(max_length=30)
    category = models.CharField(max_length=50)
    product_name = models.CharField(max_length=200)
    sales = models.FloatField()
    quantity = models.IntegerField()
    discount = models.IntegerField()
    profit = models.FloatField()


    