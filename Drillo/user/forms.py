from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django.contrib.auth import authenticate
import re

class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "class": "border border-gray-200 w-11/12 mb-1 rounded-md p-1 hover:border-gray-500 hover:border-2", 'placeholder': "Enter username"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "border border-gray-200 w-11/12 mb-1 rounded-md p-1 hover:border-gray-500 hover:border-2", 'placeholder': "Enter password"
            }
        )
    )

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "border border-gray-200 w-11/12 mb-1 rounded-md p-1 hover:border-gray-500 hover:border-2", 'placeholder': "Enter username"
            }
        )
    )
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "border border-gray-200 w-11/12 mb-1 rounded-md p-1 hover:border-gray-500 hover:border-2", 'placeholder': "Enter Password"
            }
        ),
        help_text="Your password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one numeric digit.",
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "border border-gray-200 w-11/12 mb-1 rounded-md p-1 hover:border-gray-500 hover:border-2", 'placeholder': "Confirm Password"
            }
        ),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "border border-gray-200 w-11/12 mb-1 rounded-md p-1 hover:border-gray-500 hover:border-2", 'placeholder': "Enter email"
            }
        )
    )

    branch = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "border border-gray-200 w-11/12 mb-1 rounded-md p-1 hover:border-gray-500 hover:border-2", 'placeholder': "Enter Branch"
            }
        )
    )

    library_ID = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "border border-gray-200 w-11/12 mb-1 rounded-md p-1 hover:border-gray-500 hover:border-2", 'placeholder': "Enter Library ID"
            }
        )
    )

    github = forms.URLField(
        widget=forms.URLInput(
            attrs={
                "class": "border border-gray-200 w-11/12 mb-1 rounded-md p-1 hover:border-gray-500 hover:border-2", 'placeholder': "Enter Github Profile"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'branch', 'library_ID', 'github', 'is_coordinator')

# class CustomAuthenticationForm(AuthenticationForm):
#     def clean(self):
#         username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')

#         if username and password:
#             user = authenticate(username=username, password=password)
#             if user:
#                 self.user_cache = user
#                 if user.is_coordinator:
#                     return self.cleaned_data
#                 else:
#                     raise forms.ValidationError("You are not authorized to login as a coordinator.")
#             else:
#                 raise forms.ValidationError("Invalid username or password.")
#         return self.cleaned_data

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 8:
            raise forms.ValidationError("Your password must be at least 8 characters long.")
        if not re.search("[A-Z]", password1):
            raise forms.ValidationError("Your password must contain at least one uppercase letter.")
        if not re.search("[a-z]", password1):
            raise forms.ValidationError("Your password must contain at least one lowercase letter.")
        if not re.search("[0-9]", password1):
            raise forms.ValidationError("Your password must contain at least one numeric digit.")
        if not re.search("[!@#$%^&*(),.?\":{}|<>]", password1):
            raise forms.ValidationError("Your password must contain at least one special character.")
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("The two password fields didn't match.")
        return password2