from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import EmailField, EmailInput


class SignupForm(UserCreationForm):
    email = EmailField(widget=EmailInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']  # 'phone_number'
