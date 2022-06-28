from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import *
from AppCoder.forms import formularioEstudiante, formularioProfesor

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")

def lineaDeInvestigacion(request):
    return render(request, "AppCoder/lineaDeInvestigacion.html")

def beca(request):
    return render(request, "AppCoder/beca.html")

def crearProfesor(request):
    if request.method == "POST":
        miFormulario = formularioProfesor(request.POST) #aquí mellega toda la información del html
        print(miFormulario)

        if miFormulario.is_valid:   #Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'],email=informacion['email'], profesion=informacion['profesion']) 
            profesor.save()
            return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

    else: 
        miFormulario= formularioProfesor() #Formulario vacio para construir el html

    return render(request, "AppCoder/profesores.html", {"miFormulario":miFormulario})

def crearEstudiante(request):
    if request.method == "POST":
        miFormulario = formularioEstudiante(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            estudiante = Estudiante(nombre=informacion['nombre'], apellido=informacion['apellido'], fechaCumple=informacion['fechaCumple'],email=informacion['email'])
            estudiante.save()
            return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

    else: 
        miFormulario= formularioEstudiante()
    
    return render(request,"AppCoder/estudiantes.html", {"miFormulario":miFormulario})

def busquedaEstudiante(request):
    return render(request, "AppCoder/busqueda.html")


def buscar(request):

    if request.GET['nombre']:
       nombre = request.GET['nombre']
       print(nombre)
       estudiantes = Estudiante.objects.filter(nombre__icontains=nombre)
       print(estudiantes)
       return render(request,"AppCoder/busqueda.html",{"estudiantes":estudiantes,"nombre":nombre})

    else:
      respuesta = "No enviaste datos"

    return render(request, "AppCoder/inicio.html", {"respuesta":respuesta})


