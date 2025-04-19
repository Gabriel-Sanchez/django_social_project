from django.shortcuts import render
from django.http import JsonResponse
from .models import Evento, TeamMember, Servicio
from django.utils import timezone
from datetime import timedelta

# Create your views here.

def get_upcoming_events(limit=3):
    now = timezone.now()
    return Evento.objects.filter(fecha__gte=now).order_by('fecha')[:limit]

def home(request):
    servicios = Servicio.objects.filter(activo=True)
    eventos_proximos = get_upcoming_events()
    context = {
        'servicios': servicios,
        'eventos_proximos': eventos_proximos,
        'is_home': True,  # Marcador para identificar la página principal
    }
    return render(request, 'eventsApp/home.html', context)

def events(request):
    eventos = Evento.objects.all().order_by('-fecha')
    context = {
        'eventos': eventos,
    }
    return render(request, 'eventsApp/events.html', context)

def calendar_events(request):
    eventos = Evento.objects.all()
    events_list = []
    for evento in eventos:
        events_list.append({
            'title': evento.titulo,
            'start': evento.fecha.isoformat(),
            'description': evento.descripcion,
            'location': evento.lugar,
        })
    return JsonResponse(events_list, safe=False)

def informacion_general(request):
    sacerdotes = TeamMember.objects.filter(rol='sacerdote', activo=True)
    diaconos = TeamMember.objects.filter(rol='diacono', activo=True)
    administrativos = TeamMember.objects.filter(rol='administrativo', activo=True)
    
    context = {
        'sacerdotes': sacerdotes,
        'diaconos': diaconos,
        'administrativos': administrativos,
    }
    return render(request, 'eventsApp/informacion_general.html', context)

def servicios(request):
    servicios = Servicio.objects.filter(activo=True)
    context = {
        'servicios': servicios,
    }
    return render(request, 'eventsApp/servicios.html', context)

def eventos_calendario_api(request):
    eventos = Evento.objects.all()
    data = []
    for evento in eventos:
        data.append({
            'title': evento.titulo,
            'start': evento.fecha.isoformat(),
            'description': evento.descripcion,
            'location': evento.lugar
        })
    return JsonResponse(data, safe=False)