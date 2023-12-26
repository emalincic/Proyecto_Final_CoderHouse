from django.urls import path

from AppCoder.views import show_html, agregar_profesor, agregar_alumno, ProfesorEliminar, \
    ProfesorActualizacion, \
    buscar_profesor, buscar_alumno, AboutView, ProjectView, AlumnoActualizacion, AlumnoEliminar, \
    comentarios

urlpatterns = [
    path('show/', show_html, name='home'),
    path('Profesor/', agregar_profesor),
    path('Alumno/', agregar_alumno),
    path('buscar_profesor/', buscar_profesor, name='buscar_profesor'),
    path('buscar_alumno/', buscar_alumno, name='buscar_alumno'),
    path('editar_profesor/<int:pk>', ProfesorActualizacion.as_view(), name='ProfesorEditar'),
    path('eliminar_profesor/<int:pk>', ProfesorEliminar.as_view(), name='ProfesorEliminar'),
    path('editar_alumno/<int:pk>', AlumnoActualizacion.as_view(), name='AlumnoEditar'),
    path('eliminar_alumno/<int:pk>', AlumnoEliminar.as_view(), name='AlumnoEliminar'),
    path('comentarios/', comentarios, name='comentarios'),
    path('about/', AboutView.as_view()),
    path('project/', ProjectView.as_view()),
]
