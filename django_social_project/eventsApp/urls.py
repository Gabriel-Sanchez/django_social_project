from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calendario/', views.events, name='events'),
    path('calendario/api/', views.calendar_events, name='calendar_events'),
    path('informacion-general/', views.informacion_general, name='informacion_general'),
    path('servicios/', views.servicios, name='servicios'),
]
