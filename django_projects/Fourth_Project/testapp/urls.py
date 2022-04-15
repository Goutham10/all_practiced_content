from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('save_details/', views.save_details, name = "save_details"),
    path('mart_details/', views.mart_details, name = "mart_details")
]