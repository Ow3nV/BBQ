from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import EmailValidator, RegexValidator


# Create your forms here.

class NewUserForm(UserCreationForm):
    username = forms.CharField(validators=[RegexValidator(regex=r'^[a-z]+$', message='gay'),])
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=True, help_text="Enter your username")
    password = forms.CharField(widget=forms.PasswordInput, required=True, help_text="Enter your password.")