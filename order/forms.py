from django.forms import ModelForm


class OrderForm(ModelForm):
    class Meta:
        fields = '__all__'
        exclude = ('user', 'barbeque', 'completed', 'subtotal', 'paid')
