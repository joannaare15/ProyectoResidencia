from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=128)  # Encriptado opcional
    sexo = models.CharField(max_length=10, choices=[("Masculino", "Masculino"), ("Femenino", "Femenino"), ("Otro", "Otro")], blank=True)

    

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Direccion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    calle = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)

class Soporte(models.Model):
    descripcion = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class CategoriaProducto(models.Model):
    nombre_categoria = models.CharField(max_length=100)

class Vendedor(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)  # ← este campo es necesario
    

class Reseña(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    comentario = models.TextField()
    calificacion = models.IntegerField()

class CarritoCompra(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_creacion = models.DateField()

class CarritoProducto(models.Model):
    carrito = models.ForeignKey(CarritoCompra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    class Meta:
        unique_together = ('carrito', 'producto')

class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    fecha_pedido = models.DateField()

class Envio(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    metodo_envio = models.CharField(max_length=100)
    fecha_envio = models.DateField()

class DatosPago(models.Model):
    TIPO_CHOICES = (
        ('Tarjeta', 'Tarjeta'),
        ('PayPal', 'PayPal'),
    )
    tipo_metodo = models.CharField(max_length=50, choices=TIPO_CHOICES)

class Pago(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    datos_pago = models.ForeignKey(DatosPago, on_delete=models.CASCADE)
    fecha_pago = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)

class Tarjeta(models.Model):
    datos_pago = models.OneToOneField(DatosPago, on_delete=models.CASCADE, primary_key=True)
    numero_tarjeta = models.CharField(max_length=20)
    fecha_expiracion = models.DateField()
    cvv = models.CharField(max_length=4)

class PayPal(models.Model):
    datos_pago = models.OneToOneField(DatosPago, on_delete=models.CASCADE, primary_key=True)
    correo_paypal = models.CharField(max_length=100)


    
    
    

    
    

