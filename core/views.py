from tkinter import Image
from django.shortcuts import render, redirect
from .models import Usuario, Producto
from .forms import AgregarProductoForm, EliminarProductoForm
from .forms import EditarProdcutoForm
from django.contrib import messages
import re
from django.http import JsonResponse, HttpResponse


def inicio(request):
    request.session.flush()
    return render(request, "core/pages/get_size.html")


def como_funciona(request):
    return render(request, "core/pages/como_funciona.html")


def ingreso(request):
    request.session.flush()

    if request.method == "POST":
        nombre_usuario = request.POST.get("nombreusuario")
        contraseña = hash(request.POST.get("contraseña"))

        try:
            usuario = Usuario.objects.get(
                nombre_usuario=nombre_usuario, contraseña=contraseña
            )
            request.session["id_usuario"] = usuario.pk
            return redirect("mi_tienda")
        except Usuario.DoesNotExist:
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
        contraseña = hash(request.POST.get("pass"))

        if Usuario.objects.filter(nombre_usuario=nombre_usuario).exists():
            messages.error(
                request, "El nombre de usuario ya está en uso. Por favor, elige otro."
            )
            return redirect("registro")
        if Usuario.objects.filter(mail=request.POST.get("correo")).exists():
            messages.error(request, "Ese correo ya esta en uso")
            return redirect("registro")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", request.POST.get("correo")):
            messages.error(request, "Ingrese un email")
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

        messages.success(request, "¡Registro exitoso!")
        return redirect("ingreso")

    return render(request, "core/pages/form_registro_usuario.html")


def video(request, size):
    context = {"small": 768, "med": 1024, "size": size}
    return render(request, "core/pages/template_video_index.html", context)


def mi_tienda(request):
    if request.method == "POST":
        agregar_form = AgregarProductoForm(request.POST, request.FILES)
        editar_form = EditarProdcutoForm(request.POST, request.FILES)
        eliminar_form = EliminarProductoForm(request.POST, request.FILES)
        if "editar-producto" in request.POST:
            titulo = request.POST.get("titulo")
            editar_form.fields["titulo"].choices = [(titulo, titulo)]
            if editar_form.is_valid():
                usuario_prod = Usuario.objects.get(pk=request.session["id_usuario"])
                producto_editado = Producto.objects.get(
                    usuario_prod=usuario_prod, titulo=request.POST.get("titulo")
                )
                producto_editado.descripcion = editar_form.cleaned_data["descripcion"]
                producto_editado.precio = editar_form.cleaned_data["precio"]
                if editar_form.cleaned_data["foto1"]:
                    producto_editado.foto1 = editar_form.cleaned_data["foto1"]
                    if editar_form.cleaned_data["foto2"]:
                        producto_editado.foto2 = editar_form.cleaned_data["foto2"]
                        if editar_form.cleaned_data["foto3"]:
                            producto_editado.foto3 = editar_form.cleaned_data["foto3"]

                producto_editado.save()
        if "agregar-producto" in request.POST:
            if Producto.objects.filter(titulo=agregar_form.data["titulo"]).exists():
                messages.error(
                    request,
                    "Ya tienes un producto con ese nombre. Por favor, elige otro.",
                )
                return redirect("mi_tienda")
            if agregar_form.is_valid():
                usuario_prod = Usuario.objects.get(pk=request.session["id_usuario"])
                titulo = agregar_form.cleaned_data["titulo"]
                descripcion = agregar_form.cleaned_data["descripcion"]
                precio = agregar_form.cleaned_data["precio"]
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
        if "eliminar-producto" in request.POST:
            titulo = request.POST.get("titulo")
            usuario_prod = Usuario.objects.get(pk=request.session["id_usuario"])
            producto_eliminado = Producto.objects.get(
                usuario_prod=usuario_prod, titulo=request.POST.get("titulo")
            )
            producto_eliminado.delete()
        return redirect("mi_tienda")
    else:
        agregar_form = AgregarProductoForm()
        editar_form = EditarProdcutoForm()
        eliminar_form = EliminarProductoForm()
        choices = []
        if "id_usuario" in request.session:
            request.session["productos"] = []

            productos = []
            for producto in Producto.objects.filter(
                usuario_prod=Usuario.objects.get(pk=request.session["id_usuario"])
            ):
                productos.append(producto)
                choices.append((producto.titulo, producto.titulo))

                # falta seguir lo que viene aca

            editar_form.get_choices(choices)
            eliminar_form.get_choices(choices)
            context = {
                "productos": productos,
                "agregar_form": agregar_form,
                "editar_form": editar_form,
                "eliminar_form": eliminar_form,
            }
        else:
            return redirect("ingreso")
    return render(request, "core/Pages/mi_tienda.html", context)


def get_productos(request, filter):
    res = []
    for producto in Producto.objects.filter(titulo__icontains=filter):
        titulo = str(producto.titulo)
        desc = str(producto.descripcion)
        precio = str(producto.precio)
        links = []
        links.append(f"{(hash(str(producto.pk)))}_1")
        id = producto.usuario_prod.pk
        if producto.foto2:
            links.append(f"{(hash(str(producto.pk)))}_2")
            if producto.foto3:
                links.append(f"{(hash(str(producto.pk)))}_3")
        prod = {
            "titulo": titulo,
            "precio": precio,
            "descripcion": desc,
            "links": links,
            "id": id,
        }
        res.append(prod)
    return JsonResponse({"res": res})


def get_image(request, code, foto):
    for producto in Producto.objects.all():
        prod = producto.foto1
        pk = hash(str(producto.pk))
        if int(code) == pk and foto == 1:
            prod = producto.foto1
            break
        elif int(code) == pk and foto == 2:
            prod = producto.foto2
            break
        elif int(code) == pk and foto == 3:
            prod = producto.foto3
            break
    if prod:
        return HttpResponse(prod, content_type="image/jpeg")
    else:
        return HttpResponse("")


def get_usuario(request, user):
    usuario = Usuario.objects.get(pk=int(user))
    res = [usuario.nombre_usuario, usuario.mail]
    return JsonResponse({"usuario": res})
