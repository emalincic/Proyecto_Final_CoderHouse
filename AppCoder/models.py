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


class Comentario(models.Model):
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_publicacion']

    def __str__(self):
        return f"{self.autor} - {self.fecha_publicacion}"