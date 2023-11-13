
from django.urls import path
from . import views


urlpatterns = [
   
    path('',views.inicio, name='inicio' ),
    path('valioso_mango/Pages/ComoFunciona/', views.ComoFunciona,name='como_funciona'),
]
