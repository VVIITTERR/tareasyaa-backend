from django.contrib import admin
from .models import PerfilUsuario

@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'plan', 'suscripcion_activa', 'consultas_usadas_mes', 'fecha_registro']
    list_filter = ['plan', 'suscripcion_activa', 'pais']
    search_fields = ['usuario__username', 'usuario__email', 'universidad', 'carrera']
    date_hierarchy = 'fecha_registro'