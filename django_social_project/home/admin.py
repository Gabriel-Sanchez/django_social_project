from django.contrib import admin

# Register your models here.
from .models import Contacto

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'asunto', 'fecha_envio')
    list_filter = ('fecha_envio',)
    search_fields = ('nombre', 'correo', 'asunto')