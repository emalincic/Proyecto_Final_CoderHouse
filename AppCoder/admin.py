from django.contrib import admin
from AppCoder.models import Alumno, Profesor, Comentario
from accounts.models import Avatar

admin.site.register(Profesor)

admin.site.register(Alumno)

admin.site.register(Avatar)

admin.site.register(Comentario)


