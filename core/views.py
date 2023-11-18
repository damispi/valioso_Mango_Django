from django.shortcuts import render

from django.http import HttpResponse


def inicio(request):
    return render(request, "core/Pages/get_size.html")


def ComoFunciona(request):
    return render(request, "core/Pages/ComoFunciona.html")

def ingreso(request):
    return render(request, "core/Pages/ingreso.html")

def registro(request):
    return render(request, "core/Pages/registro_usuario.html")

def video(request,size):
    context={
        'small':768,
        'med':1024,
        'size':size
    }
    return render(request, "core/Pages/template_video_index.html",context)

def mi_tienda(request):
    return render(request, "core/Pages/MiTienda.html")
# Create your views here.
