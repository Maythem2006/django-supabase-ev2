#Definir un formulario para el modelo producto, parala crear y editar de productos en las vistas
from django import forms
from .models import Producto
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'cantidad']