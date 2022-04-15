import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','thirdproject.settings')
                                                #project_name
import django
django.setup()

from testapp.models import *
from faker import Faker
from random import *

faker = Faker()

def generate(n):
    for i in range(n):
        f_eno = randint(1001,9999)
        f_ename = faker.name()
        f_esal = randint(10000,40000)
        f_eaddress = faker.city()

        emp_record = Employee.objects.get_or_create(eno =f_eno, ename= f_ename, esal = f_esal, eaddress = f_eaddress)
                     #model_name or table_name
generate(30)