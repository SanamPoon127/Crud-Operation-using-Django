from django import forms
from .models import User

class StudentRegistation(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets ={
            'name' : forms.TextInput(attrs={'class':'form-control'}),# this is done by watching html class name
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput( render_value=True, attrs={'class':'form-control'}),
        }