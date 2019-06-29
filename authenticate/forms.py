from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    """
    class SignupForm to help model user input into a user model
    that can be stored in the database
    """
    class Meta:
        model=User
        fields=('username','email','password1','password2')