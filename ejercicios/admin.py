from django.contrib import admin
from .models import Categoria, Ejercicio

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug', 'icono', 'orden', 'activo']
    list_filter = ['activo']
    search_fields = ['nombre', 'descripcion']
    prepopulated_fields = {'slug': ('nombre',)}

@admin.register(Ejercicio)
class EjercicioAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'usuario', 'categoria', 'estado', 'fecha_creacion']
    list_filter = ['estado', 'categoria', 'fecha_creacion']
    search_fields = ['titulo', 'descripcion', 'usuario__username']
    date_hierarchy = 'fecha_creacion'
    readonly_fields = ['fecha_creacion', 'fecha_actualizacion']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('usuario', 'categoria', 'titulo', 'descripcion')
        }),
        ('Archivos', {
            'fields': ('imagen', 'archivo')
        }),
        ('Estado', {
            'fields': ('estado',)
        }),
        ('Solución', {
            'fields': ('solucion_texto', 'solucion_imagen', 'solucion_pdf'),
            'classes': ('collapse',)
        }),
        ('Valoración', {
            'fields': ('valoracion',),
            'classes': ('collapse',)
        }),
        ('Fechas', {
            'fields': ('fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )