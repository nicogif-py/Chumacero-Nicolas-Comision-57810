from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *

from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, "entidades/index.html")

#___ Maestrías
@login_required
def maestrias(request):
    contexto = {"maestrias": Maestrias.objects.all() }
    return render(request, "entidades/maestrias.html", contexto)
@login_required
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
@login_required
def maestriasUpdate(request, id_maestrias):
    maestrias = Maestrias.objects.get(id=id_maestrias)
    if request.method == "POST":
        miForm = MaestriasForm(request.POST)
        if miForm.is_valid():
            maestrias.nombre = miForm.cleaned_data.get("nombre")
            maestrias.modalidad = miForm.cleaned_data.get("modalidad")
            maestrias.save()
            contexto = {"maestrias": Maestrias.objects.all() }
            return render(request, "entidades/maestrias.html", contexto)       
    else:
        miForm = MaestriasForm(initial={"nombre": maestrias.nombre, "modalidad": maestrias.modalidad}) 
    
    return render(request, "entidades/maestriasForm.html", {"form": miForm})
@login_required
def maestriasDelete(request, id_maestrias):
    maestrias = Maestrias.objects.get(id=id_maestrias)
    maestrias.delete()
    contexto = {"maestrias": Maestrias.objects.all() }
    return render(request, "entidades/maestrias.html", contexto)

#___ Alumno
@login_required
def alumno(request):
    contexto = {"alumno": Alumno.objects.all() }
    return render(request, "entidades/alumno.html", contexto)
@login_required
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
@login_required
def alumnoUpdate(request, id_alumno):
    alumno = Alumno.objects.get(id=id_alumno)
    if request.method == "POST":
        miForm = AlumnoForm(request.POST)
        if miForm.is_valid():
            alumno.nombre = miForm.cleaned_data.get("nombre")
            alumno.apellido = miForm.cleaned_data.get("apellido")
            alumno.codigo = miForm.cleaned_data.get("codigo")
            alumno.maestria = miForm.cleaned_data.get("maestria")
            alumno.save()
            contexto = {"alumno": Alumno.objects.all() }
            return render(request, "entidades/alumno.html", contexto)       
    else:
        miForm = AlumnoForm(initial={"nombre": alumno.nombre, "apellido": alumno.apellido, "codigo": alumno.codigo, "maestria": alumno.maestria,}) 
    
    return render(request, "entidades/alumnoForm.html", {"form": miForm})
@login_required
def alumnoDelete(request, id_alumno):
    alumno = Alumno.objects.get(id=id_alumno)
    alumno.delete()
    contexto = {"alumno": Alumno.objects.all() }
    return render(request, "entidades/alumno.html", contexto)

#___ Trabajo de grado
@login_required
def trabajodegrado(request):
    contexto = {"trabajodegrado": TrabajoDeGrado.objects.all() }
    return render(request, "entidades/trabajodegrado.html", contexto)
@login_required
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

class TrabajoDeGradoList(LoginRequiredMixin, ListView):
    model = TrabajoDeGrado

class TrabajoDeGradoCreate(LoginRequiredMixin, CreateView):
    model = TrabajoDeGrado
    fields = ["titulo", "tipo", "aprobado"]
    success_url = reverse_lazy("trabajodegrado")

class TrabajoDeGradoUpdate(LoginRequiredMixin, UpdateView):
    model = TrabajoDeGrado
    fields = ["titulo", "tipo", "aprobado"]
    success_url = reverse_lazy("trabajodegrado")

class TrabajoDeGradoDelete(LoginRequiredMixin, DeleteView):
    model = TrabajoDeGrado
    fields = ["titulo", "tipo", "aprobado"]
    success_url = reverse_lazy("trabajodegrado")

#___ Sustentación
@login_required
def sustentacion(request):
    contexto = {"sustentacion": Sustentacion.objects.all() }
    return render(request, "entidades/sustentacion.html", contexto)
@login_required
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

class SustentacionList(LoginRequiredMixin, ListView):
    model = Sustentacion

class SustentacionCreate(LoginRequiredMixin, CreateView):
    model = Sustentacion
    fields = ["fecha_sust", "lugar", "mencion"]
    success_url = reverse_lazy("sustentacion")

class SustentacionUpdate(LoginRequiredMixin, UpdateView):
    model = Sustentacion
    fields = ["fecha_sust", "lugar", "mencion"]
    success_url = reverse_lazy("sustentacion")

class SustentacionDelete(LoginRequiredMixin, DeleteView):
    model = Sustentacion
    fields = ["fecha_sust", "lugar", "mencion"]
    success_url = reverse_lazy("sustentacion")

#Buscar
@login_required
def buscarMaestrias(request):
    return render(request, "entidades/buscar.html")
@login_required
def encontrarMaestrias(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        maestrias = Maestrias.objects.filter(nombre__icontains=patron)
        contexto = {'maestrias': maestrias}
    else:
        contexto = {'maestrias': Maestrias.objects.all() }


    return render(request, "entidades/maestrias.html", contexto)


#Login / Logout / Registration

def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            return render(request, "entidades/index.html")
        else:
            return redirect(reverse_lazy('login'))

    else:
        miForm = AuthenticationForm()

    return render(request, "entidades/login.html", {"form": miForm})

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForm()

    return render(request, "entidades/registro.html", {"form": miForm})

#Edición de Perfil / Avatar

@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("home"))
    else:
        miForm = UserEditForm(instance=usuario)
    return render(request, "entidades/editarPerfil.html", {"form": miForm})
    
