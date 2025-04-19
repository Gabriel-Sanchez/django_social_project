from django.contrib import admin

# Register your models here.
from .models import Evento, TeamMember, Servicio

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'lugar')
    list_filter = ('fecha',)
    search_fields = ('titulo', 'lugar', 'descripcion')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rol', 'orden', 'activo')
    list_filter = ('rol', 'activo')
    search_fields = ('nombre', 'descripcion')
    list_editable = ('orden', 'activo')

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'horario', 'orden', 'activo')
    list_filter = ('activo',)
    search_fields = ('nombre', 'descripcion', 'requisitos')
    list_editable = ('orden', 'activo')