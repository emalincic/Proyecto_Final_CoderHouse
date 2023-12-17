from django.urls import path

from AppCoder.views import show_html, agregar_profesor, agregar_alumno, ProfesorList, ProfesorEliminar, \
    ProfesorActualizacion, \
    buscar_profesor, buscar_alumno, AboutView, ProjectView

urlpatterns = [
    path('show/', show_html),
    path('Profesor/', agregar_profesor),
    path('Alumno/', agregar_alumno),
    path('buscar_profesor/', buscar_profesor, name='buscar_profesor'),
    path('buscar_alumno/', buscar_alumno, name='buscar_profesor'),
    path('profesores/listar', ProfesorList.as_view(), name="ProfesorList"),
    path('editar/<int:pk>', ProfesorActualizacion.as_view(), name="ProfesorEditar"),
    path('eliminar/<int:pk>', ProfesorEliminar.as_view(), name="ProfesorEliminar"),
    path('about/', AboutView.as_view()),
    path('project/', ProjectView.as_view()),

]
