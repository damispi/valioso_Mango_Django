from django.db import models

 
class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=50, unique=True)
    contraseña = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50, null=True, blank=True)
    nombre = models.CharField(max_length=50, null=True, blank=True)
    fnac = models.DateField()
    mail = models.EmailField()
    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"
    
    
    def __str__(self):
        return self.nombre_usuario
    


class Producto(models.Model):
    usuario_prod = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(
        max_length=50, help_text="Ingrese un Título para producto "
    )
    descripcion = models.CharField(
        max_length=100, help_text="Ingrese una descripcion del producto"
    )
    precio= models.DecimalField(max_digits=6, decimal_places=2)
    foto1 = models.ImageField(upload_to="valioso_Mapp")
    foto2 = models.ImageField(default=None, upload_to="valioso_Mapp", null=True)
    foto3 = models.ImageField(default=None, upload_to="valioso_Mapp", null=True)
    create = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def __str__(self):
        return self.titulo


