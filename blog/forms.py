from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Post

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
