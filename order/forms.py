from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import ModelForm, SelectDateWidget

from order.models import Order


class OrderForm(ModelForm):
    date_from = forms.DateField(widget=SelectDateWidget(empty_label=("Choose Day", "Choose Month", "Choose Year")))
    date_to = forms.DateField(widget=SelectDateWidget(empty_label=("Choose Day", "Choose Month", "Choose Year")))
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ('user', 'barbeque', 'completed', 'sub_total', 'paid')
