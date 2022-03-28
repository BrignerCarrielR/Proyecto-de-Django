from logging import exception
from django.shortcuts import redirect, render, HttpResponse
from .forms import CargoForm,DepartamentoForm,EmpleadoForm
from .models import Cargo,Departamento,Empleado

# Create your views here.
def inicio(request):
    # return HttpResponse("<h1>Bienvenido a mi Sitio Wed</h1>")
    return render(request, "inicio.html")

#¡ todo relacionado con Cargo
def cargo(request):
    return render(request,"pages/cargo.html")

def crearCargo(request):
    if request.method =="POST":
        print("entro por post")
        cargo_form= CargoForm(request.POST)
        if cargo_form.is_valid():
            cargo_form.save()
            return redirect('cargoLista')
    else:
        print("entro por get")
    cargo_form= CargoForm()
    cargos=Cargo.objects.all()
    return render(request,"pages/cargo.html",{'cargoForm':cargo_form, 'cargos':cargos ,'accion':'Crear'})
    

def editarCargo(request,id):
    error,cargo_form=None,None
    try:
        cargo=Cargo.objects.get(id=id)
        if request.method== "GET":
            cargo_form=CargoForm(instance=cargo)
        else:
            cargo_form= CargoForm(request.POST,instance=cargo)
            if cargo_form.is_valid():
                cargo_form.save()
                return redirect('cargoLista')
    except Exception as e:
        error=e
    cargos=Cargo.objects.all()
    return render(request,"pages/cargo.html",{'cargoForm':cargo_form, 'cargos':cargos ,'accion':'Actualizar'})

def eliminarCargo(request,id):
    cargo= Cargo.objects.get(id=id)
    if request.method== "POST":
        print(cargo)
        cargo.delete()
        return redirect("cargoLista")
    return render (request,'pages/eliminar_cargo.html',{'cargo':cargo})

#¡ todo relacionado con departamento
def departamento(request):
    return render(request,"pages/departamento.html")

def crearDepartamento(request):
        if request.method =="POST":
            print("entro por post")
            departamento_form= DepartamentoForm(request.POST)
            if departamento_form.is_valid():
                departamento_form.save()
                return redirect('departamentoLista')
        else:
            print("entro por get")
        departamento_form= DepartamentoForm()
        departamentos=Departamento.objects.all()
        return render(request,"pages/departamento.html",{'departamentoForm':departamento_form, 'departamentos':departamentos ,'accion':'Crear'})

def editarDepartamento(request,id):
    error,departamento_form=None,None
    try:
        departamento=Departamento.objects.get(id=id)
        if request.method== "GET":
            departamento_form=DepartamentoForm(instance=departamento)
        else:
            departamento_form=DepartamentoForm(request.POST,instance=departamento)
            if departamento_form.is_valid():
                departamento_form.save()
                return redirect('departamentoLista')
    except Exception as e:
        error=e
    departamentos=Departamento.objects.filter(estado=True)
    return render(request,"pages/departamento.html",{'departamentoForm':departamento_form, 'departamentos':departamentos ,'accion':'Actualizar'})

def eliminarDepartamento(request,id):
    departamento= Departamento.objects.get(id=id)
    if request.method== "POST":
        print(departamento)
        departamento.delete()
        return redirect("departamento")
    return render (request,'pages/eliminar_departamento.html',{'departamento':departamento})

#¡ todo relacionado con empleado
def empleado(request):
    return render(request,"pages/empleado.html")

def crearEmpleado(request):
        if request.method =="POST":
            print("entro por post")
            empleado_form= EmpleadoForm(request.POST)
            if empleado_form.is_valid():
                empleado_form.save()
                return redirect('empleadoLista')
        else:
            print("entro por get")
        empleado_form= EmpleadoForm()
        empleados=Empleado.objects.all()
        return render(request,"pages/empleado.html",{'empleadoForm':empleado_form, 'empleados':empleados ,'accion':'Crear'})

def editarEmpleado(request,id):
    error,empleado_form=None,None
    try:
        empleado=Empleado.objects.get(id=id)
        if request.method== "GET":
            empleado_form=EmpleadoForm(instance=empleado)
        else:
            empleado_form=EmpleadoForm(request.POST,instance=empleado)
            if empleado_form.is_valid():
                empleado_form.save()
                return redirect('empleadoLista')
    except Exception as e:
        error=e
    empleados=Empleado.objects.filter(estado=True)
    return render(request,"pages/empleado.html",{'empleadoForm':empleado_form, 'empleados':empleados ,'accion':'Actualizar'})

def eliminarEmpleado(request,id):
    empleado= Empleado.objects.get(id=id)
    if request.method== "POST":
        print(empleado)
        empleado.delete()
        return redirect("empleadoLista")
    return render (request,'pages/eliminar_empleado.html',{'empleado':empleado})

def listaCargo(request):
    if request.method =="POST":
        print("entro por post")
        cargo_form= CargoForm(request.POST)
        if cargo_form.is_valid():
            cargo_form.save()
    else:
        print("entro por get")
    cargo_form= CargoForm()
    cargos=Cargo.objects.all()
    return render(request,"pages/cargoLista.html",{'cargoForm':cargo_form, 'cargos':cargos ,'accion':'Crear'})
    
def listaDepartamento(request):
    if request.method =="POST":
        print("entro por post")
        departamento_form= DepartamentoForm(request.POST)
        if departamento_form.is_valid():
            departamento_form.save()
    else:
        print("entro por get")
    departamento_form= DepartamentoForm()
    departamentos=Departamento.objects.all()
    return render(request,"pages/departamentoLista.html",{'departamentoForm':departamento_form, 'departamentos':departamentos ,'accion':'Crear'})

def listaEmpleado(request):
    if request.method =="POST":
        print("entro por post")
        empleado_form= EmpleadoForm(request.POST)
        if empleado_form.is_valid():
            empleado_form.save()
    else:
        print("entro por get")
    empleado_form= EmpleadoForm()
    empleados=Empleado.objects.all()
    return render(request,"pages/empleadoLista.html",{'empleadoForm':empleado_form, 'empleados':empleados ,'accion':'Crear'})