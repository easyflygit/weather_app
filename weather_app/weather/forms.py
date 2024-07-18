from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CityForm(forms.Form):
    city = forms.CharField(label='City', max_length=100,
                           widget=forms.TextInput(attrs={'id': 'id_city'}))


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)