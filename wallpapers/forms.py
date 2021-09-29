from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from .models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ["user_name", "user_email", "text"]
        labels = {
            "user_name": "Name",
            "user_email": "Email",
            "text": "Comment"
        }


class RegisterForm(UserCreationForm):

    username = forms.TextInput(attrs={'class': 'form-control'})
    email = forms.CharField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    # passing bootstrap class name to attrs to design in custom way.
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control '}))
    password2 = forms.CharField(label="Confirm Password (again)",
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            "username": "Name",
            "email": "Email",
        }


class LoginForm(AuthenticationForm):

    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=("Password"), widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))
