from django.db import models
from django.contrib.auth.models import User

class Pago(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('completado', 'Completado'),
        ('fallido', 'Fallido'),
    ]
    
    METODO_CHOICES = [
        ('stripe', 'Stripe'),
        ('mercadopago', 'Mercado Pago'),
        ('yape', 'Yape'),
        ('plin', 'Plin'),
    ]
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pagos')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    moneda = models.CharField(max_length=10, default='USD')
    metodo_pago = models.CharField(max_length=20, choices=METODO_CHOICES)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    plan = models.CharField(max_length=20)
    
    stripe_payment_id = models.CharField(max_length=200, blank=True)
    mercadopago_payment_id = models.CharField(max_length=200, blank=True)
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_completado = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.usuario.username} - ${self.monto} - {self.estado}"