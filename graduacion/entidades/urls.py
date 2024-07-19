from django.urls import path, include
from entidades.views import *

urlpatterns = [
    path('', home, name="home"),
    path('maestrias/', maestrias, name="maestrias"),
    path('alumno/', alumno, name="alumno"),
    path('trabajodegrado/', trabajodegrado, name="trabajodegrado"),
    path('sustentacion/', sustentacion, name="sustentacion"),

#Formularios
path('maestriasForm/', maestriasForm, name="maestriasForm"),
path('alumnoForm/', alumnoForm, name="alumnoForm"),
path('trabajodegradoForm/', trabajodegradoForm, name="trabajodegradoForm"),
path('sustentacionForm/', sustentacionForm, name="sustentacionForm"),

#Buscar
path('buscarMaestrias/', buscarMaestrias, name="buscarMaestrias"),
path('encontrarMaestrias/', encontrarMaestrias, name="encontrarMaestrias"),
]   