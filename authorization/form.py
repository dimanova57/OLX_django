from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField, EmailInput

from .models import Person


class SignupForm(UserCreationForm):
    email = EmailField(widget=EmailInput)

    class Meta:
        model = Person
        fields = ['username', 'password1', 'password2', 'email', 'phone_number']
