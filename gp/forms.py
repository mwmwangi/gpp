import email

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from gp.models import Commerce, Subscriber


class CommerceForm(forms.ModelForm):
    class Meta:
        model = Commerce
        fields= ['name','email','subject','message']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email'}),
           ' subject': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Message'}),


        }


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
        }

# from django import forms

class MpesaForm(forms.Form):
    phone_number = forms.CharField(label="Phone Number", max_length=13)
    amount = forms.IntegerField(label="Amount")


