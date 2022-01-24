from django import forms
from django.contrib.auth.models import User
from . import models

class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model=models.Customer
        fields=['username','address','mobile']
    
#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Phone=forms.IntegerField
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

class CarloaneligibilityForm(forms.Form):
    Bangladeshi = forms.CharField(max_length=100)
    Username = forms.CharField(max_length=100)
    Age	= forms.CharField(max_length=100)
    Number = forms.CharField(max_length=100)
    Gender = forms.CharField(max_length=100)
    Net_income = forms.CharField(max_length=100)
    Email = forms.CharField(max_length=100)