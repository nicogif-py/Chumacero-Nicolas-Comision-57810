from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class MaestriasForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    modalidad = forms.CharField(max_length=50)

class AlumnoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    codigo = forms.IntegerField()
    maestria = forms.CharField(max_length=100)

class TrabajoDeGradoForm(forms.Form):
    titulo = forms.CharField(max_length=200)
    tipo = forms.CharField(max_length=30)
    aprobado = forms.BooleanField()

class SustentacionForm(forms.Form):
    fecha_sust = forms.DateField() 
    lugar = forms.CharField(max_length=30)
    mencion = forms.CharField(max_length=100)

class RegistroForm(UserCreationForm):
    first_name = forms.CharField(required=True, label="Nombre")
    last_name = forms.CharField(required=True, label="Apellido")
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]

class UserEditForm(UserChangeForm):
    first_name = forms.CharField(label="Nombre", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido", max_length=50, required=True)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]