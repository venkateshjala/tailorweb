from django import forms
from .models import PaymentMode, Product,MeasurementMaster,Customer



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['id', 'name', 'gender', 'price', 'image', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'id': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }        


class MeasurementMasterForm(forms.ModelForm):
    class Meta:
        model = MeasurementMaster
        fields = ['name', 'unit']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Chest'}),
            'unit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. inches'}),
        }        


class PaymentModeForm(forms.ModelForm):
    class Meta:
        model = PaymentMode
        fields = ['name', 'is_cash', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Credit Card'}),
            'is_cash': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }        