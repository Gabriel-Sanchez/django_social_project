from django.urls import path
from . import views

urlpatterns = [
    path('', views.events, name='events'),  # Ruta principal
    path('api/calendar-events/', views.get_calendar_events, name='calendar_events'),
]
