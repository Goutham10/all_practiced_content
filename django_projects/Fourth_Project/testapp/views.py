from django.shortcuts import  redirect, render
from . import models

# Create your views here.

def index(request):
    return render(request, 'index.html')

def save_details(request):
    if request.method == 'POST':
        order_id = request.POST['order_id']
        order_date =request.POST['order_date']
        ship_date = request.POST['ship_date']
        ship_mode = request.POST['ship_mode']
        customer_id = request.POST['customer_id']
        customer_name = request.POST['customer_name']
        segment = request.POST['segment']
        country = request.POST['country']
        city = request.POST['city']
        state = request.POST['state']
        postal_code = request.POST['postal_code']
        region = request.POST['region']
        product_id = request.POST['product_id']
        category = request.POST['category']
        product_name = request.POST['product_name']
        sales = request.POST['sales']
        quantity = request.POST['quantity']
        discount = request.POST['discount']
        profit = request.POST['profit']
        
        mart = models.Supermarket.objects.create(
            order_id = order_id,
            order_date = order_date,
            ship_date = ship_date,
            ship_mode = ship_mode,
            customer_id = customer_id,
            customer_name = customer_name,
            segment = segment,
            country = country,
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

        mart.save()

        return redirect('index')
    
def mart_details(request):
    
    mart_details = models.Supermarket()
    temp = mart_details.objects.all()
    print(mart_details)
    print('hijkhdjksdjkds')
    return render(request, 'mart_details.html', {'mart_details': temp})