from django import forms
from .models import Usuario, Producto


class AgregarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ("titulo", "descripcion", "precio", "foto1", "foto2", "foto3")
        labels = {
            "nombre": "Nombre",
            "descripcion": "Descripcion",
            "precio": "Precio",
            "foto1": "",
            "foto2": "",
            "foto3": "",
        }
        widgets = {}

