from django.db import models

# Modelo del proceso de graduación
class Maestrias(models.Model):
    nombre = models.CharField(max_length=100)
    modalidad = models.CharField(max_length=50)

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    codigo = models.IntegerField()
    maestria = models.CharField(max_length=100)

class TrabajoDeGrado(models.Model):
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=30)
    aprobado = models.BooleanField()

class Sustentacion(models.Model):
    fecha_sust = models.DateField()
    lugar = models.CharField(max_length=30)
    mencion = models.CharField(max_length=100)

