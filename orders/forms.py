from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    username = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Username', "rows": 1, "cols": 40, 'style': 'width: 300px;', 'class': 'form-control'}))
    price = forms.DecimalField(widget=forms.TextInput(
        attrs={'placeholder': 'Price', 'style': 'width: 300px;', 'class': 'form-control'}))
    items = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Items', "rows": 2, "cols": 40, 'style': 'width: 300px;', 'class': 'form-control'}))
    instruction_restaurant = forms.CharField(widget=forms.Textarea(
        attrs={'required': False, 'placeholder': 'Instruction for restaurant', "rows": 2, "cols": 40, 'style': 'width: 300px;', 'class': 'form-control'}))
    instruction_delivery = forms.CharField(widget=forms.Textarea(
        attrs={'required': False, 'placeholder': 'Instruction for delivery', "rows": 2, "cols": 40, 'style': 'width: 300px;', 'class': 'form-control'}))
    prep_time = forms.DecimalField(widget=forms.TextInput(
        attrs={'placeholder': 'Preparation Time', 'style': 'width: 300px;', 'class': 'form-control'}))

    class Meta:
        model = Order
        fields = [
            'username',
            'items',
            'price',
            'instruction_restaurant',
            'instruction_delivery',
            'prep_time'
        ]
