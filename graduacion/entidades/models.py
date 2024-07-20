from django.db import models
from django.contrib.auth.models import User

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

    def __str__(self):
        return f"{self.titulo}"

class Sustentacion(models.Model):
    fecha_sust = models.DateField()
    lugar = models.CharField(max_length=30)
    mencion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.fecha_sust} en {self.lugar}"


class Avatar(models.Model):   
    imagen = models.ImageField(upload_to="avatares") 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"   