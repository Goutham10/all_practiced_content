from django import forms
from .models import Employee

class EmployeeForms(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__' #we can write fields manually (customized) ex: fields = ('fullname','mobile','emp_code','position')
        labels = {
            'full_name' : 'Full Name',
            'emp_code' : 'EMP Code'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForms,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = 'Select'
        self.fields['emp_code'].required = False