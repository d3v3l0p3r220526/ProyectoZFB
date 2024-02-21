from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm
from .models import Task



# Creando las vistas del proyecto.

def home(request):
    return render(request, 'home.html')


def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tareas')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'Usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Contraseña Incorrecta'
        })


def tareas(request):
    tasks = Task.objects.all()#filter(user=request.user, datecompleted_isnull=True)
    return render(request, 'tareas.html',{'tasks': tasks})

def create_task(request):
    if request.method == 'GET':
        return render(request,'create_task.html', {
            'form': TaskForm
        })
    else:
        try: 
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user    
            new_task.save()
            return redirect('tareas')
        except ValueError:
            return render(request,'tareas.html', {
                'form': TaskForm,
                "error": 'POr favor diligencie los datos'
            })

        
def task_detail(request):
    #task = get_object_or_404(Task, pk=task_id)
    #form = TaskForm(instance=task)
    return render(request,'task_detail.html')#, {'task': task, 'form': form})

        


def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:             
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o Clave Incorrectos'
            })
        else:
            login(request, user)
            return redirect('tareas')