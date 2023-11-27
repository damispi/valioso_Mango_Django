from django.urls import path
from . import views


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("inicio", views.inicio, name="inicio"),
    path("valioso_mango/Pages/como_funciona/", views.como_funciona, name="como_funciona"),
    path("ingreso", views.ingreso, name="ingreso"),
    path("registro", views.registro, name="registro"),
    path("<int:size>", views.video, name="video"),
    path("mi_tienda/", views.mi_tienda, name="mi_tienda"),
]
