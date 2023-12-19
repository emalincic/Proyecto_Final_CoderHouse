from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import DeleteView, UpdateView, CreateView, ListView, DetailView, TemplateView

from AppCoder.forms import ProfesorForm, AlumnoForm, Busqueda
from AppCoder.models import Profesor, Alumno
from AppCoder.forms import Busqueda


@login_required(login_url='Login')
def show_html(request):
    contexto = {}
    return render(request, 'index.html', contexto)


def no_hay_nada(request):
    return render(request, 'AppCoder/error404.html')


class AboutView(TemplateView):
    template_name = "AppCoder/about.html"


class ProjectView(TemplateView):
    template_name = "AppCoder/project.html"


def agregar_profesor(request):
    if request.method == "POST":
        profesorform = ProfesorForm(request.POST)
        if profesorform.is_valid():
            info = profesorform.cleaned_data
            profesores = Profesor(nombre=info["nombre"], apellido=info["apellido"], profesor_de=info["profesor_de"],
                                  fecha_nacimiento=info["fecha_nacimiento"], mail=info["mail"])
            profesores.save()

            return redirect("/app/show/#page-top")

    form_profesor = ProfesorForm()
    contexto = {
        "form": form_profesor
    }

    return render(request, "AppCoder/Agregar_profesor.html", contexto)


def agregar_alumno(request):
    if request.method == "POST":
        alumnoform = AlumnoForm(request.POST)
        if alumnoform.is_valid():
            info = alumnoform.cleaned_data
            alumno_agregar = Alumno(nombre=info["nombre"], apellido=info["apellido"],
                                    fecha_nacimiento=info["fecha_nacimiento"], mail=info["mail"])
            alumno_agregar.save()

            return redirect("/app/show/#page-top")

    form_alumno = AlumnoForm()
    contexto = {
        "form": form_alumno
    }

    return render(request, "AppCoder/Agregar_alumno.html", contexto)


def buscar_profesor(request):
    form = Busqueda(request.GET or None)
    profesores = Profesor.objects.all()
    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        profesores = Profesor.objects.filter(nombre__icontains=nombre)

    return render(request, "AppCoder/buscar_profesor.html", {'form': form, 'profesores': profesores})


def buscar_alumno(request):
    form = Busqueda(request.GET or None)
    alumnos = Alumno.objects.all()
    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        alumnos = Profesor.objects.filter(nombre__icontains=nombre)

    return render(request, "AppCoder/buscar_alumno.html", {'form': form, 'alumnos': alumnos})


class ProfesorActualizacion(UpdateView):
    model = Profesor
    success_url = "/buscar_profesor"
    template_name = "AppCoder/Agregar_profesor.html"
    fields = ["nombre", "apellido", "profesor_de", "fecha_nacimiento", "mail"]


class ProfesorEliminar(DeleteView):
    model = Profesor
    template_name = "AppCoder/Eliminar_profesor.html"
    success_url = "/app/buscar_profesor"


class AlumnoActualizacion(UpdateView):
    model = Alumno
    success_url = "/buscar_alumno"
    template_name = "AppCoder/Agregar_alumno.html"
    fields = ["nombre", "apellido", "fecha_nacimiento", "mail"]


class AlumnoEliminar(DeleteView):
    model = Alumno
    template_name = "AppCoder/Eliminar_alumno.html"
    success_url = "/app/buscar_alumno"
