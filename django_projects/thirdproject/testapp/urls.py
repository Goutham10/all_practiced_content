from django.urls import path
from testapp import views

urlpatterns = [
    path('date_time_view/',views.date_time_view, name='date_time_view'),
    path('testing1/', views.testing1, name="testing1"),
    path('', views.employee_info_view, name='employee_info_view')
    
]