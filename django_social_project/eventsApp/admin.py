from django.contrib import admin

# Register your models here.
from .models import Evento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'lugar', 'creado_en')
    list_filter = ('fecha',)
    search_fields = ('titulo', 'descripcion', 'lugar')