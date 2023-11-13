from django.shortcuts import render

from django.http import HttpResponse


def inicio(request):
    return render(request, "core/index.html")


def ComoFunciona(request):
    return render(request, "core/Pages/ComoFunciona.html")


# Create your views here.
