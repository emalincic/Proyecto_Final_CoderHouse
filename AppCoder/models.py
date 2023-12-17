from django.db import models


class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    profesor_de = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    mail = models.EmailField()


class Alumno(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    mail = models.EmailField()
