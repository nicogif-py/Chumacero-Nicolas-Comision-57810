from django import forms

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