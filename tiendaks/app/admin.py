from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Producto)
admin.site.register(ImagenProducto)
admin.site.register(Carrito)
admin.site.register(ItemCarrito)