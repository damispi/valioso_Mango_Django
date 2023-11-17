from django.shortcuts import render

from django.http import HttpResponse


def inicio(request):
    return render(request, "core/index.html")


def ComoFunciona(request):
    return render(request, "core/Pages/ComoFunciona.html")

def ingreso(request):
    return render(request, "core/Pages/ingreso.html")


# Create your views here.
