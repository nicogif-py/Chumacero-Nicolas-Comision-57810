from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Maestrias)
admin.site.register(Alumno)
admin.site.register(TrabajoDeGrado)
admin.site.register(Sustentacion)