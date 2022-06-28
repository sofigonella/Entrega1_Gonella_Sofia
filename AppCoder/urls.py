from django.urls import path

from AppCoder import views

urlpatterns = [
   
    path('', views.inicio, name="inicio"), #esta era nuestra primer view
    path('beca', views.beca, name="beca"),
    path('lineaDeInvestigacion', views.lineaDeInvestigacion, name="lineaDeInvestigacion"),
    path('profesores', views.crearProfesor, name="profesores"),
    path('estudiantes', views.crearEstudiante, name="estudiantes"),
    path('busqueda', views.busquedaEstudiante, name="busqueda"),
    path('buscar/', views.buscar),
    
]
