from django.db import models

class Producto(models.Model):
    titulo=models.CharField(max_length=50,help_text="Ingrese un Título para producto ")
    descripcion=models.CharField(max_length=200,help_text="Ingrese una descripcion del producto")
    foto1=models.ImageField(upload_to='valioso_Mapp')
    foto2=models.ImageField(upload_to='valioso_Mapp')
    foto4=models.ImageField(upload_to='valioso_Mapp')
    create=models.DateTimeField(auto_now=True)
    update=models.DateTimeField(auto_now=True)
# Create your models here.
