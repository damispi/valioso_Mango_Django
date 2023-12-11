from django import forms
from .models import Producto


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


class EliminarProductoForm(forms.Form):
    titulo = forms.ChoiceField(widget=forms.Select())

    def get_choices(self, *args):
        choices = []
        for arg in args:
            choices = arg
        self.fields["titulo"].choices = choices


class EditarProdcutoForm(EliminarProductoForm):
    titulo = forms.ChoiceField(widget=forms.Select())
    descripcion = forms.CharField(
        max_length=100, help_text="Ingrese una descripcion del producto"
    )
    precio = forms.DecimalField(
        max_digits=6, decimal_places=2, help_text="Precio del producto en mangos"
    )
    foto1 = forms.ImageField(required=False)
    foto2 = forms.ImageField(required=False)
    foto3 = forms.ImageField(required=False)
