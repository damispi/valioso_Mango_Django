from django.db import models



class usuario(models.Model):
    nombre_usuario=models.CharField(max_length=50)
    contraseña=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    fnac=models.DateField()
    mail=models.EmailField()

    class Meta:
            verbose_name='usuario'
            verbose_name_plural='usuarios'
    
    def __str__(self):
            return self.nombre_usuario 
class Producto(models.Model):
    usuario_prod = models.ForeignKey(usuario, on_delete=models.CASCADE)
    titulo=models.CharField(max_length=50,help_text="Ingrese un Título para producto ")
    descripcion=models.CharField(max_length=100,help_text="Ingrese una descripcion del producto")
    foto1=models.ImageField(upload_to='valioso_Mapp')
    foto2=models.ImageField(upload_to='valioso_Mapp')
    foto3=models.ImageField(upload_to='valioso_Mapp')
    create=models.DateTimeField(auto_now=True)
    update=models.DateTimeField(auto_now=True)

    class Meta:
            verbose_name='producto'
            verbose_name_plural='productos'
    def __str__(self):
            return self.titulo   
    



# Create your models here.char
