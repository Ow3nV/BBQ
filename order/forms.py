from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import ModelForm, SelectDateWidget

from order.models import Order


class DateInput(forms.DateInput):
    input_type = 'date'


class OrderForm(ModelForm):
    date_from = forms.DateField(widget=DateInput)
    date_to = forms.DateField(widget=DateInput)
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ('user', 'barbeque', 'completed', 'sub_total', 'paid')
