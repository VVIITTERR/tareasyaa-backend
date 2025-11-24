from django.contrib import admin
from .models import Pago

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'monto', 'moneda', 'metodo_pago', 'estado', 'plan', 'fecha_creacion']
    list_filter = ['estado', 'metodo_pago', 'plan', 'fecha_creacion']
    search_fields = ['usuario__username', 'usuario__email', 'stripe_payment_id', 'mercadopago_payment_id']
    date_hierarchy = 'fecha_creacion'
    readonly_fields = ['fecha_creacion', 'fecha_completado']