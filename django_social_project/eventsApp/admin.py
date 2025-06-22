from django.contrib import admin

# Register your models here.
from .models import Evento, TeamMember, Servicio, CarouselImage, About, Noticia

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'lugar', 'creado_en')
    search_fields = ('titulo', 'descripcion', 'lugar')
    list_filter = ('fecha', 'creado_en')
    date_hierarchy = 'fecha'
    fieldsets = (
        ('Información básica', {
            'fields': ('titulo', 'fecha', 'lugar', 'descripcion')
        }),
        ('Contenido detallado', {
            'fields': ('contenido_detallado',),
            'classes': ('collapse',)
        }),
    )

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

@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'orden', 'activo', 'fecha_actualizacion')
    list_editable = ('orden', 'activo')
    list_filter = ('activo',)
    search_fields = ('titulo', 'subtitulo')
    ordering = ['orden', '-fecha_creacion']

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion', 'activo', 'destacada')
    list_filter = ('activo', 'destacada', 'autor', 'fecha_publicacion')
    search_fields = ('titulo', 'resumen', 'contenido')
    list_editable = ('activo', 'destacada')
    date_hierarchy = 'fecha_publicacion'
    fieldsets = (
        ('Información Principal', {
            'fields': ('titulo', 'resumen', 'autor', 'imagen')
        }),
        ('Contenido', {
            'fields': ('contenido',)
        }),
        ('Estado', {
            'fields': ('activo', 'destacada')
        }),
    )

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'activo', 'fecha_actualizacion')
    list_editable = ('activo',)
    fieldsets = (
        ('Información General', {
            'fields': ('objetivo', 'mision', 'vision')
        }),
        ('Historia', {
            'fields': ('historia',)
        }),
        ('Estado', {
            'fields': ('activo',)
        }),
    )