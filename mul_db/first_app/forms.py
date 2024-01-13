from first_app.models import employee_model
from django import forms

class Employee_create_form(forms.ModelForm):
    class Meta:
        model=employee_model
        fields='__all__'



class Employee_read_form(forms.ModelForm):
    class Meta:
        model=employee_model
        fields=['employee_id',]

