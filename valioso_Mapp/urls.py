
from django.urls import path
from . import views


urlpatterns = [
   
    path('',views.inicio),
    path('valioso_Mapp/Pages/ComoFunciona/', views.ComoFunciona,name='como_funciona'),
]
