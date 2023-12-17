from django import forms


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
