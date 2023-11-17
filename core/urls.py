from django.urls import path
from . import views


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("valioso_mango/Pages/ComoFunciona/", views.ComoFunciona, name="como_funciona"),
    path("ingreso", views.ingreso, name="ingreso"),
    path("registro", views.registro, name="registro"),
    path("<int:size>", views.video, name="video")
]
