from tkinter import Widget
from django import forms
from.models import Cargo, Departamento, Empleado

class CargoForm(forms.ModelForm):
    class Meta:
        model=Cargo
        fields=['descripcion','estado']
        widgets={
            'descripcion':forms.TextInput(attrs={
                'placeholder':'Ingrese Cargo',
                'class':'form-group',
                'required':True
            })
        }

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model=Departamento
        fields=['descripcion','estado']
        widgets={
            'descripcion':forms.TextInput(attrs={
                'placeholder':'Ingrese Departamento',
                'class':'form-group',
                'required':True
            })
        }

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model=Empleado
        fields=['nombre','cedula','cargo','departamento','sueldo','estado']
        widgets={
            'nombre':forms.TextInput(attrs={
                'placeholder':'Ingrese Nombre',
                'class':'form-group',
                'required':True}),
            'cedula':forms.NumberInput(attrs={
                'placeholder':'Ingrese Cédula',
                'class':'form-group',
                'required':True,
                }),
            'sueldo':forms.TextInput(attrs={
                'placeholder':'Ingrese Sueldo',
                'class':'form-group',
                'required':True}),
        }
            
                    
