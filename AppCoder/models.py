from django.db import models

class Estudiante(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    fechaCumple = models.DateField()
    email= models.EmailField()

class Profesor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)

class LineaDeInvestigacion(models.Model):
    nombreLinea = models.CharField(max_length=30)

class Beca(models.Model):
    tipoDeBeca = models.CharField(max_length=30)