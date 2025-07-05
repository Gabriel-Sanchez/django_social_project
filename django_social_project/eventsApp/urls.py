from django.urls import path
from . import views, ckeditor_views

urlpatterns = [
    path('inicio/', views.home, name='inicio'),
    path('eventos/', views.events, name='events'),
    path('eventos/<int:event_id>/', views.event_detail, name='event_detail'),
    path('eventos/calendario/', views.calendar_events, name='calendar_events'),
    path('eventos/calendario/api/', views.eventos_calendario_api, name='eventos_calendario_api'),
    path('informacion/mision-vision-valores/', views.mision_vision_valores, name='mision_vision_valores'),
    path('informacion/ubicacion/', views.ubicacion, name='ubicacion'),
    path('informacion/equipo-pastoral/', views.equipo_pastoral, name='equipo_pastoral'),
    path('informacion/historia/', views.historia, name='historia'),
    path('informacion/fundaciones-hermanas/', views.fundaciones_hermanas, name='fundaciones_hermanas'),
    path('contacto/', views.contacto, name='contacto'),
    path('contacto/donaciones/', views.donaciones, name='donaciones'),
    path('servicios/', views.servicios, name='servicios'),
    path('cooperacion/', views.cooperacion, name='cooperacion'),
    path('ayuda-humanitaria/', views.ayuda_humanitaria, name='ayuda_humanitaria'),
    path('accion-social/', views.accion_social, name='accion_social'),
    path('educacion-sensibilizacion/', views.educacion_sensibilizacion, name='educacion_sensibilizacion'),
    path('comercio-justo/', views.comercio_justo, name='comercio_justo'),
    path('noticias/', views.noticias, name='noticias'),
    path('noticias/<int:noticia_id>/', views.noticia_detail, name='noticia_detail'),
    
    # URLs personalizadas para CKEditor con validación
    path('ckeditor/upload/', ckeditor_views.ckeditor_upload, name='ckeditor_upload'),
    path('ckeditor/browse/', ckeditor_views.ckeditor_browse, name='ckeditor_browse'),
    
    path('', views.home, name='index'),  # Redirige la raíz a inicio
]
