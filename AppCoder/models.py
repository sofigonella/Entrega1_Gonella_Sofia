from django.db import models
from django.contrib.auth.models import User

class Estudiante(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    fechaCumple = models.DateField()
    email= models.EmailField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - Fecha Cumple {self.fechaCumple} - E-Mail {self.email}"
        
class Profesor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - E-Mail: {self.email} - Profesion: {self.profesion}"

class LineaDeInvestigacion(models.Model):
    nombreLinea = models.CharField(max_length=30)

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)