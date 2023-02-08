from django.shortcuts import render
from django.http import HttpResponse
from Appcoder.models import Curso

#def curso(self):
    #curso=Curso(nombre="Python",camada=23800)
    #curso.save()
    #doctexto=f'---> Curso {curso.nombre}, camada {curso.camada}'
    #return HttpResponse(doctexto)#

def inicio(request):
    return render(request,'Template/Appcoder/inicio.html')
    #return HttpResponse('Vista Inicio')

def cursos(request):
    return render(request,'Appcoder/cursos.html')
    #return HttpResponse('Vista Cursos')
def profesores(request):
    return render(request,'Appcoder/profesores.html')
    #return HttpResponse('Vista profesores')   
def entregables(request):
    return render(request,'Appcoder/entregables.html')
    #return HttpResponse('Vista entregables') 
def estudiantes(request):
    return render(request,'Appcoder/estudiantes.html')
    #return HttpResponse('Vista estudiantes  ')    