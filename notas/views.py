from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from . import forms
# the homepage


def home(request):
    context = {'title': 'Instituto Tecnologico Unemi'}
    return render(request, 'home.html', context)


def register(request):
    if request.method == 'GET':
        context = {'title': 'Registro de Usuario',
                   'form': UserCreationForm(), 'photo': forms.profileForm()}
        return render(request, 'register.html', context)
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'])
                user.save()
                profile = UserProfile(user=user, photo=request.POST['photo'])
                profile.save()
                # crea una cooki del usuario registrado
                login(request, user)
                return redirect('home')
            except IntegrityError:
                context = {'title': 'Registro de Usuario',
                           'form': UserCreationForm(
                               request.POST), 'photo': forms.profileForm(),
                           'error': 'Usuario ya existe'}
                return render(request, 'register.html', context)
        context = {'title': 'Registro de Usuario',
                   'form': UserCreationForm(
                       request.POST), 'photo': forms.profileForm(),
                   'error': 'Password no coinciden'}
        return render(request, 'register.html', context)


def iniciarSesion(request):
    if request.method == 'GET':
        context = {'title': 'Iniciar Sesion',
                   'form': AuthenticationForm}
        return render(request, 'login.html', context)
    else:
        print(request.POST)
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            context = {'title': 'Iniciar Sesion', 'form': AuthenticationForm,
                       'error': 'Usuario o password incorrecto'}
            return render(request, 'login.html', context)
        else:
            # crea una cooki del usuario registrado - guardar session
            login(request, user)
            return redirect('home')


@login_required
def cerrarSesion(request):
    logout(request)
    return redirect('login')

# crud the students
