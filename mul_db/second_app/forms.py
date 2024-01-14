from second_app.models import Student_model
from django import forms

class Student_create_form(forms.ModelForm):
    class Meta:
        model=Student_model
        fields='__all__'



class Student_read_form(forms.ModelForm):
    class Meta:
        model=Student_model
        fields=['student_id',]

