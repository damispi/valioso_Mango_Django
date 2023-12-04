from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("inicio", views.inicio, name="inicio"),
    path(
        "valioso_mango/Pages/como_funciona/", views.como_funciona, name="como_funciona"
    ),
    path("ingreso", views.ingreso, name="ingreso"),
    path("registro", views.registro, name="registro"),
    path("<int:size>", views.video, name="video"),
    path("mi_tienda", views.mi_tienda, name="mi_tienda"),
    path("get_productos_<str:filter>", views.get_productos, name="get_productos"),
    path("<str:code>_<int:foto>", views.get_image, name="get_image"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
