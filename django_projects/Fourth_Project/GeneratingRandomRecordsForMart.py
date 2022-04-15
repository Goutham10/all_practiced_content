import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Fourth_Project.settings')
                                                #project_name
import django
django.setup()

from testapp.models import *
from faker import Faker
from random import *

faker = Faker()

def generate(n):
    for i in range(n):
        order_id = faker.name()[:3].upper() + str(randint(101,9999))
        order_date = faker.date()
        ship_date = faker.date()
        ship_mode = faker.random_element(elements=('First Class', 'Second Class', 'Standard Class'))
        customer_id = faker.name()[:3].upper() +"-"+ str(randint(1001, 9999))
        customer_name = faker.name()
        segment = faker.random_element(elements=('Consumer', 'Corporate', 'Home Office'))
        country = faker.country()
        city = faker.city()
        state = faker.state()
        postal_code = randint(500231,800231)
        region = faker.random_element(elements=('South', 'North', 'East', 'West', 'Central'))
        product_id = faker.name()[:3].upper() +"-"+faker.name()[:2].upper()+"-"+ str(randint(100001, 999999))
        category = faker.random_element(elements=('Furniture', 'Office Supplies', 'Technology'))
        product_name = faker.random_element(elements=(  'Bush Somerset Collection Bookcase',
                                                        'Hon Deluxe Fabric Upholstered Stacking Chairs, Rounded Back',
                                                        'Self-Adhesive Address Labels for Typewriters by Universal',
                                                        'Bretford CR4500 Series Slim Rectangular Table',
                                                        'Eldon Fold \'N Roll Cart System',
                                                        'Eldon Expressions Wood and Plastic Desk Accessories, Cherry Wood',
                                                        'Newell 322',
                                                        'Mitel 5320 IP Phone VoIP phone',
                                                        'DXL Angle-View Binders with Locking Rings by Samsill',
                                                        'Belkin F5C206VTEL 6 Outlet Surge',
                                                        'Chromcraft Rectangular Conference Tables',
                                                        'Konftel 250 Conference phone - Charcoal black',
                                                        'Xerox 1967',
                                                        'Fellowes PB200 Plastic Comb Binding Machine',
                                                        'Holmes Replacement Filter for HEPA Air Cleaner, Very Large Room, HEPA Filter',
                                                        'Storex DuraTech Recycled Plastic Frosted Binders',
                                                        'Stur-D-Stor Shelving, Vertical 5-Shelf: 72"H x 36"W x 18 1/2"D',
                                                        'Fellowes Super Stor/Drawer',
                                                        'Newell 341',
                                                        'Cisco SPA 501G IP Phone',
                                                        'Wilson Jones Hanging View Binder, White, 1"',
                                                        'Newell 318',
                                                        'Acco Six-Outlet Power Strip, 4\' Cord Length',
                                                        'Global Deluxe Stacking Chair, Gray',
                                                        'Bretford CR4500 Series Slim Rectangular Table',
                                                        'Wilson Jones Active Use Binders',
                                                        'Imation 8GB Mini TravelDrive USB 2.0 Flash Drive',
                                                        'Riverside Palais Royal Lawyers Bookcase, Royale Cherry Finish',
                                                        'Avery Recycled Flexi-View Covers for Binding Systems'))
        sales = float(str(randint(2,999)) +"."+ str(randint(99,999)))
        quantity = randint(1,99)
        discount = randint(1,99)
        profit = float(str(randint(0,99)) +"."+ str(randint(99,999)))
        mart_record = Supermarket.objects.get_or_create(
                                                        order_id = order_id,
                                                        order_date = order_date,
                                                        ship_date = ship_date,
                                                        ship_mode = ship_mode,
                                                        customer_id = customer_id,
                                                        customer_name = customer_name,
                                                        segment = segment,
                                                        country= country,
                                                        city = city,
                                                        state = state,
                                                        postal_code = postal_code,
                                                        region = region,
                                                        product_id = product_id,
                                                        category = category,
                                                        product_name = product_name,
                                                        sales = sales,
                                                        quantity = quantity,
                                                        discount = discount,
                                                        profit = profit
                                                        )
generate(1)