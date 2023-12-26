from django import forms

from AppCoder.models import Comentario


class ProfesorForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    profesor_de = forms.CharField()
    fecha_nacimiento = forms.DateField()
    mail = forms.EmailField()


class AlumnoForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    fecha_nacimiento = forms.DateField()
    mail = forms.EmailField()


class Busqueda(forms.Form):
    nombre = forms.CharField()


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'contenido']

    # Widgets para personalizar el formulario con CSS
    widgets = {
        'contenido': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe un comentario'}),

    }
