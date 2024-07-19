from django.shortcuts import render
from .models import *

from .forms import *

# Create your views here.
def home(request):
    return render(request, "entidades/index.html")


def maestrias(request):
    contexto = {"maestrias": Maestrias.objects.all() }
    return render(request, "entidades/maestrias.html", contexto)

def alumno(request):
    return render(request, "entidades/alumno.html")

def trabajodegrado(request):
    return render(request, "entidades/trabajodegrado.html")

def sustentacion(request):
    return render(request, "entidades/sustentacion.html")

#Formularios
def maestriasForm(request):
    if request.method == "POST":
        miForm = MaestriasForm(request.POST)
        if miForm.is_valid():
            maestria_nombre = miForm.cleaned_data.get("nombre")
            maestria_modalidad = miForm.cleaned_data.get("modalidad")
            
            maestrias = Maestrias(nombre = maestria_nombre, modalidad = maestria_modalidad)
            maestrias.save()
            contexto = {"maestrias": Maestrias.objects.all() }
            return render(request, "entidades/maestrias.html", contexto)
    else:
        miForm = MaestriasForm()

    return render(request, "entidades/maestriasForm.html", {"form": miForm})


def alumnoForm(request):
    if request.method == "POST":
        miForm = AlumnoForm(request.POST)
        if miForm.is_valid():
            alumno_nombre = miForm.cleaned_data.get("nombre")
            alumno_apellido = miForm.cleaned_data.get("apellido")
            alumno_codigo = miForm.cleaned_data.get("codigo")
            alumno_maestria = miForm.cleaned_data.get("maestria")
           
            alumno = Alumno(nombre = alumno_nombre, apellido = alumno_apellido, codigo = alumno_codigo, maestria = alumno_maestria)
            alumno.save()
            contexto = {"alumno": Alumno.objects.all() }
            return render(request, "entidades/alumno.html", contexto)
    else:
        miForm = AlumnoForm()

    return render(request, "entidades/alumnoForm.html", {"form": miForm})


def trabajodegradoForm(request):
    if request.method == "POST":
        miForm = TrabajoDeGradoForm(request.POST)
        if miForm.is_valid():
            trabajodegrado_titulo = miForm.cleaned_data.get("titulo")
            trabajodegrado_tipo = miForm.cleaned_data.get("tipo")
            trabajodegrado_aprobado = miForm.cleaned_data.get("aprobado")
           
            trabajodegrado = TrabajoDeGrado(titulo = trabajodegrado_titulo, tipo = trabajodegrado_tipo, aprobado = trabajodegrado_aprobado)
            trabajodegrado.save()
            contexto = {"trabajodegrado": TrabajoDeGrado.objects.all() }
            return render(request, "entidades/trabajodegrado.html", contexto)
    else:
        miForm = TrabajoDeGradoForm()

    return render(request, "entidades/trabajodegradoForm.html", {"form": miForm})


def sustentacionForm(request):
    if request.method == "POST":
        miForm = SustentacionForm(request.POST)
        if miForm.is_valid():
            sustentacion_fecha_sust = miForm.cleaned_data.get("fecha_sust")
            sustentacion_lugar= miForm.cleaned_data.get("lugar")
            sustentacion_mencion = miForm.cleaned_data.get("mencion")
           
            sustentacion = Sustentacion(fecha_sust = sustentacion_fecha_sust, lugar = sustentacion_lugar, mencion = sustentacion_mencion)
            sustentacion.save()
            contexto = {"sustentacion": Sustentacion.objects.all() }
            return render(request, "entidades/sustentacion.html", contexto)
    else:
        miForm = SustentacionForm()

    return render(request, "entidades/sustentacionForm.html", {"form": miForm})


#Buscar
def buscarMaestrias(request):
    return render(request, "entidades/buscar.html")

def encontrarMaestrias(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        maestrias = Maestrias.objects.filter(nombre__icontains=patron)
        contexto = {'maestrias': maestrias}
    else:
        contexto = {'maestrias': Maestrias.objects.all() }


    return render(request, "entidades/maestrias.html", contexto)