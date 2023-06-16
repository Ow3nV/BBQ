from django import forms
from django.forms import ModelForm

from bbqweb.models import Barbeque, Images


MY_CHOICES = ((1, 'Butane'),
              ('Propane', 'Propane'),
              (3, 'Both'),
              (4, 'Neither'))

MY_CHOICES2 = ((1, 0),
               (2, 1),
               (3, 2),
               (4, 3),
               (5, 4),
               (6, 5),
               (7, 6),)


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
