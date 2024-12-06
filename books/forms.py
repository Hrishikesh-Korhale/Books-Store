from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'mobile', 'address']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }
