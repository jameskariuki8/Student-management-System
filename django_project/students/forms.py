from django import forms  
from .models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields =[ 'student_number', 'first_name', 'last_name', 'email', 'field_of_study', 'gpa']
        labels ={
            'student_number':'Student_Number',
            'first_name':'First_Name',
            'last_name': 'Last_Name',
            'email':'Email',
            'field_of_study':'Field_of_Study',
            'gpa':'GPA'
        }
        widgets = { 
          'student_number': forms.NumberInput(attrs= {  "class": "form=conrol"}),
          'first_name' : forms.TextInput(attrs={"class": "form-control"}),
          'last_name' : forms.TextInput(attrs={"class": "form-control"}), 
          'email' : forms.EmailInput(attrs={"class": "form-control"}),
          'field_of_study' : forms.TextInput(attrs={"class": "form-control"}),
          'gpa' :  forms.NumberInput(attrs= { "class": "form=conrol"}),
        }