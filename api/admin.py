from django.contrib import admin
from .models import *

admin.site.register(Usuario)
admin.site.register(Direccion)
admin.site.register(Soporte)
admin.site.register(CategoriaProducto)
admin.site.register(Vendedor)
admin.site.register(Producto)
admin.site.register(Reseña)
admin.site.register(CarritoCompra)
admin.site.register(CarritoProducto)
admin.site.register(Pedido)
admin.site.register(Envio)
admin.site.register(DatosPago)
admin.site.register(Pago)
admin.site.register(Tarjeta)
admin.site.register(PayPal)

