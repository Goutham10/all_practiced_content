from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.employee_form, name='employee_insert'), #get and post for insert operation
    path('list/',views.employee_list, name='employee_list'), #get req. to retrieve and display all records
    path('<int:id>/', views.employee_form, name='employee_update'),#get and post for update operation
    path('delete/<int:id>/', views.employee_delete, name='employee_delete')
]
