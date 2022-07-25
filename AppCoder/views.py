from sre_constants import SUCCESS
from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import *
from AppCoder.forms import UserEditForm, UserRegisterForm, formularioEstudiante, formularioProfesor

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

#@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    try:
        return render(request, "AppCoder/inicio.html", {"url":avatares[0].imagen.url} )
    except IndexError:
        return render(request, "AppCoder/inicio.html")
    
    #return render(request, "AppCoder/inicio.html",{"url": avatares[0].imagen.url})
    #return render(request, "AppCoder/inicio.html")

def profesores(request):
    profesores = Profesor.objects.all() #trae todos los profesores
    avatares = Avatar.objects.filter(user=request.user.id)
    #contexto= {"profesores":profesores}
    try:
        contexto= {"profesores":profesores,"url": avatares[0].imagen.url}
        return render(request, "AppCoder/profesores.html",contexto)
    except IndexError:
        contexto = {"profesores":profesores}
        return render(request, "AppCoder/profesores.html",contexto)
    #return render(request, "AppCoder/profesores.html",contexto)

def estudiantes(request):
    estudiantes = Estudiante.objects.all() #trae todos los profesores
    avatares = Avatar.objects.filter(user=request.user.id)
    try:
        contexto= {"estudiantes":estudiantes,"url": avatares[0].imagen.url}
        return render(request, "AppCoder/estudiantes.html",contexto)
    except IndexError:
        contexto = {"estudiantes":estudiantes}
        return render(request, "AppCoder/estudiantes.html",contexto)
    #return render(request, "AppCoder/estudiantes.html",contexto)

def AcercaDeMi(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    try:
        return render(request, "AppCoder/about.html", {"url":avatares[0].imagen.url} )
    except IndexError:
        return render(request, "AppCoder/about.html")
    #return render(request, "AppCoder/about.html",{"url": avatares[0].imagen.url})
    #return render(request, "AppCoder/about.html")

################## ADMINISTRAR ##################
@login_required
def Administrar(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "AppCoder/administrar.html",{"url": avatares[0].imagen.url})
    #return render(request, "AppCoder/administrar.html")


################## CREAR ESTUDIANTE Y PROFESOR #######################
@login_required
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
    
    return render(request,"AppCoder/crearEstudiante.html", {"miFormulario":miFormulario})

@login_required
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

    return render(request, "AppCoder/crearProfesor.html", {"miFormulario":miFormulario})

######################################################################

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


############# LEER #############
def leerProfesores(request):

      profesores = Profesor.objects.all() #trae todos los profesores

      contexto= {"profesores":profesores} 

      return render(request, "AppCoder/leerProfesores.html",contexto)

############# ELIMINAR #############
def eliminarProfesor(request,profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()

    #vuelvo al menu
    profesores = Profesor.objects.all()
    contexto ={"profesores":profesores}
    return render(request,"AppCoder/leerProfesores.html",contexto)

############# EDITAR #############
def editarProfesor(request, profesor_nombre):

      #Recibe el nombre del profesor que vamos a modificar
      profesor = Profesor.objects.get(nombre=profesor_nombre)

      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':

            miFormulario = formularioProfesor(request.POST) #aquí mellega toda la información del html
            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django
                  informacion = miFormulario.cleaned_data

                  profesor.nombre = informacion['nombre']
                  profesor.apellido = informacion['apellido']
                  profesor.email = informacion['email']
                  profesor.profesion = informacion['profesion']

                  profesor.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= formularioProfesor(initial={'nombre': profesor.nombre, 'apellido':profesor.apellido , 
            'email':profesor.email, 'profesion':profesor.profesion}) 

      #Voy al html que me permite editar
      return render(request, "AppCoder/editarProfesor.html", {"miFormulario":miFormulario, "profesor_nombre":profesor_nombre})

###########################################################################

####################### CLASES ESTUDIANTES ################################

class EstudianteList(ListView):
   model = Estudiante
   #template_name = "AppCoder/estudiante_list.html"
   template_name = "AppCoder/estudiante_list.html"
   

class EstudianteDetalle(DetailView):
   model= Estudiante
   template_name = "AppCoder/estudiante_detalle.html"

class EstudianteCreacion(CreateView):
    model = Estudiante
    #success_url = "/AppCoder/estudiante/list"
    success_url = "/AppCoder/estudiante_list"
    fields = ['nombre','apellido','fechaCumple','email']        

class EstudianteUpdate(UpdateView):
    model = Estudiante
    success_url = "/AppCoder/estudiante/list"
    fields = ['nombre', 'apellido', 'fechaCumple', 'email']

class EstudianteDelete(DeleteView):
    model = Estudiante
    success_url = "/AppCoder/estudiante/list"

##########################################################################


########################### LOGIN #################################
def login_request(request):
      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')
                  email = form.cleaned_data.get('email')
                  first_name = form.cleaned_data.get('first_name')
                  last_name = form.cleaned_data.get('last_name')        
                   
                  user = authenticate(username = usuario , password = contra)
                 
                  if user is not None:
                        login(request, user)
                        return render (request, "AppCoder/inicio.html", {"mensaje": f"Bienvenido/a {usuario}"})
                  else:
                        return render (request, "AppCoder/inicio.html", {"mensaje":"Error en los datos"})
            else:
                  return render(request, "AppCoder/inicio.html", {"mensaje":"Formulario erroneo"})
      form = AuthenticationForm()
      return render(request, "AppCoder/login.html", {'form': form})

def register(request):
      if request.method == "POST":
            form = UserRegisterForm(request.POST) 
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request, "AppCoder/inicio.html", {"mensaje": "usuario creado"})
      else: 
            form = UserRegisterForm()
            #form = UserCreationForm()
      return render(request, "AppCoder/registro.html", {"form": form})

########################## EDITAR PERFIL ######################################
@login_required
def editarPerfil(request):
      usuario = request.user
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST)
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password2']
                  usuario.save()
                  return render(request, "AppCoder/administrar.html")
      else:
            miFormulario = UserEditForm(initial={'email':usuario.email})
      return render(request, "AppCoder/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})

###############################################################################

