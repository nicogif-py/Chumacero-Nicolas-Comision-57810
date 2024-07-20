from django.urls import path, include
from entidades.views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home"),
    

#___ Maestrías
path('maestrias/', maestrias, name="maestrias"),
path('maestriasForm/', maestriasForm, name="maestriasForm"),
path('maestriasUpdate/<id_maestrias>/', maestriasUpdate, name="maestriasUpdate"),
path('maestriasDelete/<id_maestrias>/', maestriasDelete, name="maestriasDelete"),

#___ Alumno
path('alumno/', alumno, name="alumno"),
path('alumnoForm/', alumnoForm, name="alumnoForm"),
path('alumnoUpdate/<id_alumno>/', alumnoUpdate, name="alumnoUpdate"),
path('alumnoDelete/<id_alumno>/', alumnoDelete, name="alumnoDelete"),

#___ Trabajo de grado
path('trabajodegrado/', TrabajoDeGradoList.as_view(), name="trabajodegrado"),
###path('trabajodegradoForm/', trabajodegradoForm, name="trabajodegradoForm"),
path('trabajodegradoCreate/', TrabajoDeGradoCreate.as_view(), name="trabajodegradoCreate"),
path('trabajodegradoUpdate/<int:pk>', TrabajoDeGradoUpdate.as_view(), name="trabajodegradoUpdate"),
path('trabajodegradoDelete/<int:pk>', TrabajoDeGradoDelete.as_view(), name="trabajodegradoDelete"),

#___ Sustentación
path('sustentacion/', SustentacionList.as_view(), name="sustentacion"),
###path('sustentacion/', sustentacion, name="sustentacion"),
###path('sustentacionForm/', sustentacionForm, name="sustentacionForm"),
path('sustentacionCreate/', SustentacionCreate.as_view(), name="sustentacionCreate"),
path('sustentacionUpdate/<int:pk>', SustentacionUpdate.as_view(), name="sustentacionUpdate"),
path('sustentacionDelete/<int:pk>', SustentacionDelete.as_view(), name="sustentacionDelete"),


#Buscar
path('buscarMaestrias/', buscarMaestrias, name="buscarMaestrias"),
path('encontrarMaestrias/', encontrarMaestrias, name="encontrarMaestrias"),


#Login / Logout / Registration
path('login/', loginRequest, name="login"), 
path('logout/', LogoutView.as_view(template_name="entidades/logout.html"), name="logout"),
path('registro/', register, name="registro"), 

#Edición de Perfil / Avatar
path('perfil/', editProfile, name="perfil"),

]   