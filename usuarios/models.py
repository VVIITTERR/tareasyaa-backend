from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class PerfilUsuario(models.Model):
    PLAN_CHOICES = [
        ('gratuito', 'Gratuito'),
        ('basico', 'Básico - $5/mes'),
        ('premium', 'Premium - $10/mes'),
    ]
    
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    plan = models.CharField(max_length=20, choices=PLAN_CHOICES, default='gratuito')
    foto_perfil = models.ImageField(upload_to='perfiles/', blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True)
    pais = models.CharField(max_length=100, default='Peru')
    universidad = models.CharField(max_length=200, blank=True)
    carrera = models.CharField(max_length=200, blank=True)
    
    fecha_inicio_suscripcion = models.DateTimeField(null=True, blank=True)
    fecha_fin_suscripcion = models.DateTimeField(null=True, blank=True)
    suscripcion_activa = models.BooleanField(default=False)
    
    consultas_disponibles = models.IntegerField(default=3)
    consultas_usadas_mes = models.IntegerField(default=0)
    
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.usuario.username} - {self.plan}"

@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        PerfilUsuario.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_perfil_usuario(sender, instance, **kwargs):
    if hasattr(instance, 'perfil'):
        instance.perfil.save()