from django.forms import ModelForm

from bbqweb.models import Barbeque


class BarbequeForm(ModelForm):
    class Meta:
        model = Barbeque
        fields = '__all__'
