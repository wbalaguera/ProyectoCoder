from django.shortcuts import render
from django.http import HttpResponse
from Appcoder.models import Curso

#def curso(self):
    #curso=Curso(nombre="Python",camada=23800)
    #curso.save()
    #doctexto=f'---> Curso {curso.nombre}, camada {curso.camada}'
    #return HttpResponse(doctexto)#

def inicio(request):
    return HttpResponse('Vista Inicio')

def curso(request):
    return HttpResponse('Vista Cursos')
def profesores(request):
    return HttpResponse('Vista profesores')   
def entregables(request):
    return HttpResponse('Vista entregables') 
def estudiantes(request):
    return HttpResponse('Vista estudiantes  ')    