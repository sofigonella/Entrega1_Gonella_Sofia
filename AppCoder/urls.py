from django.urls import path

from AppCoder import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
   
    path('', views.inicio, name="inicio"), #esta era nuestra primer view
    path('about', views.AcercaDeMi, name="about"),
    #path('profesores', views.crearProfesor, name="profesores"),
    path('profesores', views.profesores, name="profesores"),
    path('crearProfesor', views.crearProfesor, name='crearProfesor'),
    
    path('estudiantes', views.estudiantes,  name="estudiantes"),
    path('crearEstudiante', views.crearEstudiante, name="crearEstudiante"),

    path('busqueda', views.busquedaEstudiante, name="busqueda"),
    path('buscar/', views.buscar),

    path('administrar', views.Administrar, name="administrar"),

    path('leerProfesores', views.leerProfesores, name="leerProfesores"),
    path('eliminarProfesor/<profesor_nombre>', views.eliminarProfesor, name="eliminarProfesor"),
    path('editarProfesor/<profesor_nombre>', views.editarProfesor, name="editarProfesor"),

    path('login', views.login_request, name='login'),
    path('register',views.register, name='register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name = 'logout'),

    path('estudiante/list', views.EstudianteList.as_view(), name='List'),

    path(r'^(?P<pk>\d+)$', views.EstudianteDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.EstudianteCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.EstudianteUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.EstudianteDelete.as_view(), name='Delete'),

    path('editarPerfil', views.editarPerfil, name='editarPerfil'),
]
