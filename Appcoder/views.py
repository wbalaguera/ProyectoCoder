from django.shortcuts import render
from django.http import HttpResponse
from Appcoder.models import Curso

def inicio(request):
    return render(request,'Appcoder/inicio.html')
    #return HttpResponse('Vista Inicio')

def cursos(request): 
    return render(request,'Appcoder/cursos.html')
    #return HttpResponse('Vista Cursos',name="Cursos")
def profesores(request):
    return render(request,'Appcoder/profesores.html')
    #return HttpResponse('Vista profesores')   
def entregables(request):
    return render(request,'Appcoder/entregables.html')
    #return HttpResponse('Vista entregables') 
def estudiantes(request):
    return render(request,'Appcoder/estudiantes.html')
    #return HttpResponse('Vista estudiantes  ')    
def cursoFormulario(request):
    if request.method == 'POST':
        miformulario= cursoFormulario(request.POST) #AQUI LLEGA TODA LA INFO DE L HTM
        print (miformulario)
        if miformulario.is_valid:
            informacion=miformulario.cleaned_data
            curso=Curso(nombre=informacion['curso'],camada=informacion ['camada'])
            curso.save()
        return render (request,"Appcoder/inicio.html")
    else:
        miformulario=cursoFormulario() #formulario vacio para construir el htm    
    return render(request,"Appcoder/cursoFormulario.html" ,   {"miFormulario":miformulario}      )    