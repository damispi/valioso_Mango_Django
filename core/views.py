from django.shortcuts import render



def inicio(request):
    return render(request, "core/pages/get_size.html")


def como_funciona(request):
    return render(request, "core/pages/como_funciona.html")


def ingreso(request):
    return render(request, "core/pages/form_ingreso.html")


def registro(request):
    return render(request, "core/pages/form_registro_usuario.html")


def video(request, size):
    context = {"small": 768, "med": 1024, "size": size}
    return render(request, "core/pages/template_video_index.html", context)


def mi_tienda(request):
    return render(request, "core/pages/mi_tienda.html")


# Create your views here.
