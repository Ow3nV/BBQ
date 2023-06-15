from django.forms import ModelForm

from bbqweb.models import Barbeque, Images


class BarbequeForm(ModelForm):
    class Meta:
        model = Barbeque
        fields = '__all__'


class ImageForm(ModelForm):
    class Meta:
        model = Images
        fields = '__all__'
        exclude = ('barbeque',)
