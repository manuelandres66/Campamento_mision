from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import Ingresar
from .decorators import usuario_sin_ingresar
# Create your views here.

def home(request):
    return render(request, 'home.html')

@usuario_sin_ingresar
def asesores(request):
    error = ""
    if request.method == 'POST':
        form = Ingresar(request.POST)
        if form.is_valid():
            usuario = request.POST['usuario']
            password = request.POST['password']
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                return redirect('directorio/')
            else:
                error = "Usuario y contraseña no coinciden"
        else:
            error = "Datos Invalidos"
    form = Ingresar()
    ctx = {'form' : form, 'error' : error}
    return render(request, 'asesores.html', ctx)

def salir(request):
    logout(request)
    return redirect('../../asesores/')