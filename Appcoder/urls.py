from django.urls import path
from Appcoder import views


urlpatterns = [
    path("", views.inicio),
    path("Cursos/", views.curso,name='Cursos'),
    path("Profesores/", views.profesores),
    path("Estudiantes/", views.estudiantes),
    path("Entregables/", views.entregables),
]
