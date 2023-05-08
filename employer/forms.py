from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Employer 



class EmployerForm(forms.ModelForm):
    class Meta:

        model = Employer
        fields = '__all__'
        widgets = {
            'job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'job_description': forms.Textarea(attrs={'class': 'form-control', 'rows':3}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            #'company_GST_number': forms.TextInput(attrs={'class': 'form-control'}),
            #'pancard_number':forms.TextInput(attrs={'class':'form-control'}),
            'no_of_opening': forms.NumberInput(attrs={'class': 'form-control'}),
            'experience': forms.NumberInput(attrs={'class': 'form-control'}),
            'job_location': forms.TextInput(attrs={'class': 'form-control'}),
            'qualification':forms.TextInput(attrs={'class': 'form-control'}),
            'skills': forms.TextInput(attrs={'class': 'form-control'}),
            'salary_range': forms.NumberInput(attrs={'class': 'form-control'}),
            'contact_person_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_person_profile': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'company_address': forms.Textarea(attrs={'class': 'form-control', 'rows':3}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'model_of_job': forms.Select(attrs={'class': 'form-control'}, choices=Employer.choice_of_job),
            'job_type': forms.Select(attrs={'class': 'form-control'}, choices=Employer.job_choice),
            #'upload_company_logo':forms.Upload(attrs={'class':'form-control'})
        }


class Signup(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput(attrs={'class':'form-control'}))    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email'}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }

class Login(AuthenticationForm):
    username = UsernameField(label='Username', widget=forms.TextInput(attrs={'class':'form-control', 'autofocus': True}))
    password = UsernameField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'autocomplete': 'current-password'})) 