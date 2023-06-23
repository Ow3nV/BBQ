from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import EmailValidator, RegexValidator


# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    address_line_1 = forms.CharField(max_length=50)
    address_line_2 = forms.CharField(max_length=50)
    town_city = forms.CharField(max_length=50)
    county_state = forms.CharField(max_length=50)
    country = forms.CharField(max_length=50)
    postcode = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2", "address_line_1",
                  "address_line_2", "town_city", "county_state", "country", "postcode")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=True, help_text="Enter your username")
    password = forms.CharField(widget=forms.PasswordInput, required=True, help_text="Enter your password.")