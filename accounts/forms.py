from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User

from accounts.models import Avatar


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    avatar = forms.ImageField(widget=forms.FileInput, required=False)

    class Meta:
        model = User
        fields = ("username", "email", "avatar")


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class AvatarUpdateForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ("imagen",)
        widgets = {
            'imagen': forms.FileInput(attrs={'class': 'form-control form-control-avatar'})
        }
