#Registrar el modelo Producto para volverlo accesible desde el panel de administración
from django.contrib import admin
from .models import Producto

admin.site.register(Producto)