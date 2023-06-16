from django import forms
from django.forms import ModelForm

from bbqweb.models import Barbeque, Images


MY_CHOICES = (('Butane', 'Butane'),
              ('Propane', 'Propane'),
              ('Both', 'Both'),
              ('Neither', 'Neither'))

MY_CHOICES2 = ((0, '0'),
               (1, '1'),
               (2, '2'),
               (3, '3'),
               (4, '4'),
               (5, '5'),
               (6, '6'),)


class BarbequeForm(ModelForm):
    burners = forms.ChoiceField(choices=MY_CHOICES2)
    side_burners = forms.ChoiceField(choices=MY_CHOICES2)
    gas = forms.ChoiceField(choices=MY_CHOICES)

    class Meta:
        model = Barbeque
        fields = '__all__'


class ImageForm(ModelForm):
    class Meta:
        model = Images
        fields = '__all__'
        exclude = ('barbeque',)
