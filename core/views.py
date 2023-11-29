from django.shortcuts import render, redirect
from .models import Usuario, Producto
from .forms import AgregarProductoForm
from django.contrib import messages
from django import forms
from django.http import JsonResponse


def inicio(request):
    return render(request, "core/pages/get_size.html")


def como_funciona(request):
    return render(request, "core/pages/como_funciona.html")


def ingreso(request):
    request.session["id_usuario"] = None
    request.session["productos"] = None
    if request.method == "POST":
        nombre_usuario = request.POST.get("nombreusuario")
        contraseña = request.POST.get("contraseña")
        usuario = Usuario.objects.filter(
            nombre_usuario=nombre_usuario, contraseña=contraseña
        ).first()

        if usuario:
            request.session["id_usuario"] = usuario.pk
            return redirect("mi_tienda")
        else:
            mensaje_error = "Nombre de usuario o contraseña incorrectos."
            return render(
                request,
                "core/pages/form_ingreso.html",
                {"mensaje_error": mensaje_error},
            )

    return render(request, "core/pages/form_ingreso.html")


def registro(request):
    if request.method == "POST":
        # datos del formulario
        nombre_usuario = request.POST.get("nombreusuario")
        contraseña = request.POST.get("pass")

        if Usuario.objects.filter(nombre_usuario=nombre_usuario).exists():
            messages.error(
                request, "El nombre de usuario ya está en uso. Por favor, elige otro."
            )
            return redirect("registro")

        nuevo_usuario = Usuario(
            nombre_usuario=nombre_usuario,
            contraseña=contraseña,
            apellido=request.POST.get("apellido"),
            nombre=request.POST.get("nombres"),
            fnac=request.POST.get("fecha-de-nacimiento"),
            mail=request.POST.get("correo"),
        )
        nuevo_usuario.save()
        print(nuevo_usuario)

        messages.success(request, "¡Registro exitoso!")
        return redirect("ingreso")

    return render(request, "core/pages/form_registro_usuario.html")


def video(request, size):
    context = {"small": 768, "med": 1024, "size": size}
    return render(request, "core/pages/template_video_index.html", context)


def mi_tienda(request):
    if request.method == "POST":
        agregar_form = AgregarProductoForm(request.POST, request.FILES)
        usuario_prod = Usuario.objects.get(pk=request.session["id_usuario"])
        titulo = request.POST.get("titulo")
        descripcion = request.POST.get("descripcion")
        precio = request.POST.get("precio")
        if agregar_form.is_valid():
            foto1 = agregar_form.cleaned_data["foto1"]
            foto2 = None
            foto3 = None
            if agregar_form.cleaned_data["foto2"]:
                foto2 = agregar_form.cleaned_data["foto2"]
                if agregar_form.cleaned_data["foto3"]:
                    foto3 = agregar_form.cleaned_data["foto3"]
            nuevo_producto = Producto(
                usuario_prod=usuario_prod,
                titulo=titulo,
                descripcion=descripcion,
                precio=precio,
                foto1=foto1,
                foto2=foto2,
                foto3=foto3,
            )
            nuevo_producto.save()
        return redirect("mi_tienda")
    else:
        agregar_form = AgregarProductoForm()
        if "id_usuario" in request.session:
            request.session["productos"] = []
            if "productos" in request.session:
                productos = []
                for producto in Producto.objects.filter(
                    usuario_prod=Usuario.objects.get(pk=request.session["id_usuario"])
                ):
                    productos.append(producto)
                    # falta seguir lo que viene aca
                context = {"productos": productos, "agregar_form": agregar_form}
            else:
                context = {"productos": [], "agregar_form": agregar_form}

        else:
            return redirect("ingreso")
        return render(request, "core/Pages/mi_tienda.html", context)


def get_productos(request):
    res = []
    for producto in Producto.objects.filter(
        usuario_prod=Usuario.objects.get(pk=request.session["id_usuario"])
    ):
        titulo = str(producto.titulo)
        desc = str(producto.descripcion)
        precio = str(producto.precio)
        prod = {
            'titulo':titulo,
            'precio':precio,
            'descripcion':desc
        }
        res.append(prod)
    return JsonResponse({'res':res})
