from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='insert_student'),
    path('saving_details/', views.saving_details, name='saving_details'),
    path('student_list/', views.student_list, name ='student_list'),
    path('student_update/<int:id>/', views.student_update, name='student_update'),
    path('delete/<int:id>', views.student_delete, name='student_delete'),
    path('student_updation_process/<int:id>', views.student_updation_process, name ='insert_student')
    
]