from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.events, name='events'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('calendario/api/', views.eventos_calendario_api, name='eventos_calendario_api'),
    path('informacion-general/', views.informacion_general, name='informacion_general'),
    path('servicios/', views.servicios, name='servicios'),
]
