from django import forms
from django.forms import ModelForm

from order.models import Order


CHOICES = (
    (True, 'Yes - I Want My Barbeque Delivered'),
    (False, 'No - I Will Pick Up My Barbeque')
)

CHOICES2 = (
    (True, 'Yes - I Want You To Pick Up My Barbeque After'),
    (False, 'No - I Will Drop Off My Barbeque After')
)


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ('barbeque', 'completed', 'sub_total', 'paid', 'date_to', 'date_from', 'pick_up', 'delivery')


class CalenderForm(forms.Form):
    delivery = forms.ChoiceField(choices=CHOICES)
    pickup = forms.ChoiceField(choices=CHOICES2)
