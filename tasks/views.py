# Importaciones necesarias
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

#Create your view here

# Vista principal que muestra las tareas del usuario autenticado
@login_required
def index(request):
    # Obtener todas las tareas del usuario actual
    tasks = Task.objects.filter(usuario=request.user)

    # Crear una instancia del formulario para agregar tareas
    form = TaskForm()

    # Procesar la solicitud POST al agregar una nueva tarea
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            # Guardar la tarea asociada al usuario actual
            task = form.save(commit=False)
            task.usuario = request.user
            task.save()
            return redirect('/')

    # Contexto para renderizar la plantilla
    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context)

# Vista para actualizar una tarea existente
def updateTask(request, pk):
    # Obtener la tarea por su clave primaria
    task = Task.objects.get(id=pk)
    
    # Crear una instancia del formulario con los datos actuales de la tarea
    form = TaskForm(instance=task)
    
    # Procesar la solicitud POST al actualizar la tarea
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
            
    # Contexto para renderizar la plantilla
    context = {'form': form}
    return render(request, 'tasks/update.html', context)

# Vista para eliminar una tarea
def deleteTask(request, pk):
    # Obtener la tarea por su clave primaria
    item = Task.objects.get(id=pk)
    
    # Procesar la solicitud POST al confirmar la eliminación
    if request.method == "POST":
        item.delete()
        return redirect('/')
    
    # Contexto para renderizar la plantilla de confirmación de eliminación
    context = {'item': item}
    return render(request, 'tasks/delete.html', context)

# Vista para registrar un nuevo usuario
def registrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Guardar el nuevo usuario y autenticarlo
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = UserCreationForm()
    
    # Contexto para renderizar la plantilla de registro de usuario
    return render(request, 'registration/registrar_usuario.html', {'form': form})

# Vista para iniciar sesión
def ingresar(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Credenciales incorrectas. Por favor, intenta de nuevo.')
        else:
            messages.error(request, 'Credenciales incorrectas. Por favor, intenta de nuevo.')
    else:
        form = AuthenticationForm()

    # Contexto para renderizar la plantilla de inicio de sesión
    return render(request, 'registration/login.html', {'form': form})
