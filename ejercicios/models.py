from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    icono = models.CharField(max_length=50, default='📚')
    descripcion = models.TextField(blank=True)
    orden = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = "Categorías"
        ordering = ['orden', 'nombre']
    
    def __str__(self):
        return self.nombre


class Ejercicio(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('resuelto', 'Resuelto'),
    ]
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ejercicios')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    titulo = models.CharField(max_length=300)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='ejercicios/imagenes/%Y/%m/', blank=True, null=True)
    archivo = models.FileField(upload_to='ejercicios/archivos/%Y/%m/', blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    
    solucion_texto = models.TextField(blank=True)
    solucion_imagen = models.ImageField(upload_to='soluciones/imagenes/%Y/%m/', blank=True, null=True)
    solucion_pdf = models.FileField(upload_to='soluciones/pdfs/%Y/%m/', blank=True, null=True)
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    valoracion = models.IntegerField(choices=[(i, f'{i} estrellas') for i in range(1, 6)], null=True, blank=True)
    
    class Meta:
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return f"{self.titulo} - {self.usuario.username}"