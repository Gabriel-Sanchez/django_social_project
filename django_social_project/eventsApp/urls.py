from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('calendario/api/', views.eventos_calendario_api, name='eventos_calendario_api'),
    path('mision-vision-valores/', views.mision_vision_valores, name='mision_vision_valores'),
    path('ubicacion/', views.ubicacion, name='ubicacion'),
    path('equipo-pastoral/', views.equipo_pastoral, name='equipo_pastoral'),
    path('historia/', views.historia, name='historia'),
    path('servicios/', views.servicios, name='servicios'),
]
