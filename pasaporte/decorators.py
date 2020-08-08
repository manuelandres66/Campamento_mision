from django.http import HttpResponse
from django.shortcuts import redirect

def usuario_sin_ingresar(view_func):
    def comprobador(request, *args, **kargs):
        if request.user.is_authenticated:
            return redirect('https://campamentomision.herokuapp.com/asesores/directorio')
        else:
            return view_func(request, *args, **kargs)
    return comprobador