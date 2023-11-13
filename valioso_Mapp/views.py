from django.shortcuts import render

from django.http import HttpResponse

def inicio(request):
    return render(request,"valioso_Mapp/index.html")
def ComoFunciona(request):
    return render(request,"valioso_Mapp/Pages/ComoFunciona.html")

# Create your views here.
