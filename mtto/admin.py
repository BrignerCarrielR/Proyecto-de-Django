from django.contrib import admin
from .models import Cargo,Empleado,Departamento
# Register your models here.
admin.site.register(Cargo)
admin.site.register(Departamento)
admin.site.register(Empleado)


