from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
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
    password = None
    email = forms.EmailField(label='Nuevo email', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Nueva dirección de email', 'required': False}))
    first_name = forms.CharField(label='Nombre', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nombre', 'required': False}))
    last_name = forms.CharField(label='Apellidos', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Apellidos', 'required': False}))
    username = forms.CharField(label='Nuevo Nombre de Usuario', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nuevo Nombre de Usuario', 'required': False}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class PasswordEditForm(PasswordChangeForm):
    old_password = forms.CharField(label='Contraseña actual', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Contraseña actual'}))
    new_password1 = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Nueva contraseña'}))
    new_password2 = forms.CharField(label='Repetir nueva contraseña', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Repetir nueva contraseña'}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']


class AvatarUpdateForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ("imagen",)
        widgets = {
            'imagen': forms.FileInput(attrs={'class': 'form-control form-control-avatar'})
        }
