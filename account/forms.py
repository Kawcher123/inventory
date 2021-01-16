from django.forms import ModelForm
from .models import Order,Customer,Product
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'type': 'password'
    }))


class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=('name','phone', 'email','address','status')

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control'}),

        }


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=('name','price', 'category','status','description','tags')

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
			'description':forms.Textarea(attrs={'class':'form-control'}),
			'tag':forms.Textarea(attrs={'class':'form-control'}),

        }