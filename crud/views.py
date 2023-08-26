from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import CustomUser
from django.db import IntegrityError
from .models import Empleado
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your models here.


# CURD - Empleados
@login_required
def home_crud(request):
    empleadosListados = Empleado.objects.all()
    messages.success(request, '¡Empleados listados!')
    return render(request, "projects/gestionEmpleados.html", {"empleados": empleadosListados})


@login_required
def registrarEmpleado(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']

    empleado = Empleado.objects.create(codigo=codigo,
                                 nombre=nombre,
                                 apellido=apellido)
    messages.success(request, '¡Empleados registrado!')
    return redirect('home_crud')


@login_required
def edicionEmpleado(request, codigo):
    empleado = Empleado.objects.get(codigo=codigo)
    return render(request, "projects/edicionEmpleados.html", {"empleado": empleado})


@login_required
def editarEmpleado(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']

    empleado = Empleado.objects.get(codigo=codigo)
    empleado.nombre = nombre
    empleado.apellido = apellido
    empleado.save()

    messages.success(request, '¡Empleado actualizado!')

    return redirect('home_crud')


@login_required
def eliminarEmpleado(request, codigo):
    empleado = Empleado.objects.get(codigo=codigo)
    empleado.delete()

    messages.success(request, '¡Empleado eliminado!')

    return redirect('home_crud')


# Sistema de Login/Register
def index_view(request):
    return render(request, "index.html")


def tasks_view(request):
    return render(request, 'projects/tasks.html')


def login_view(request):
    if request.method == 'POST' and 'login-form' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        print("Username:", username)
        print("Password:", password)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_crud')
        else:
            context = {'login_error': 'Username or password is incorrect'}
            return render(request, 'index.html', context)


def registro_view(request):
    if request.method == 'POST' and 'register-form' in request.POST:
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        # print(
        #     f"Name: {name}, Username: {username}, Email: {email}, Password: {password}, Confirm Password: {confirm_password}")

        if password == confirm_password:
            if CustomUser.objects.filter(username=username).exists():
                context = {'username_exists': True}
                return render(request, 'index.html', context)

            try:
                user = CustomUser.objects.create_user(
                    username=username, password=password, email=email, name=name)
                user.save()
                login(request, user)
                return redirect('home_login')
            except IntegrityError:
                context = {'error': 'User already exists'}
                return render(request, 'index.html', context)
        else:
            context = {'error': 'Password do not match'}
            return render(request, 'index.html', context)

    return render(request, 'index.html', context)

