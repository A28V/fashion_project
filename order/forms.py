from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'postal_code', 'city','address']
        labels ={
            'first_name':'',
            'last_name':'',
            'email':'',
            'postal_code':'',
            'city':'',
            'address':'',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'postal_code': forms.TextInput(attrs={'class':'form-control','placeholder':'Postal Address'}),
            'city': forms.TextInput(attrs={'class':'form-control','placeholder':'City'}),
            'address': forms.Textarea(attrs={'class':'form-control textarea','placeholder':'Address','rows':3}),
        }
