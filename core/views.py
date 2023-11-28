from django.shortcuts import render, redirect
from .models import Usuario, Producto
from django.contrib import messages


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
        usuario_prod = Usuario.objects.get(pk=request.session["id_usuario"])
        titulo = request.POST.get("titulo")
        descripcion = request.POST.get("descripcion")
        precio=request.POST.get("precio")
        foto1 = request.POST.get("fotos")
        foto2 = None
        foto3 = None
        if request.POST.get("fotos2"):
            foto2 = request.POST.get("fotos2")
            if request.POST.get("fotos3"):
                foto3 = request.POST.get("fotos3")
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
        return redirect("core/pages/mi_tienda.html")
    else:
        if "id_usuario" in request.session:
            request.session["productos"] = []
            if "productos" in request.session:
                productos = []
                for producto in Producto.objects.filter(
                    usuario_prod=Usuario.objects.get(pk=request.session["id_usuario"])
                ):
                    productos.append(producto)
                    # falta seguir lo que viene aca
                context = {"productos": productos}
            else:
                context = {"productos": []}

        else:
            return redirect("ingreso")
        return render(request, "core/pages/mi_tienda.html", context)
