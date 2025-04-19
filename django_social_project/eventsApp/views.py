from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


from .models import Evento, TeamMember, Servicio

def home(request):
    servicios = Servicio.objects.filter(activo=True)
    return render(request, 'eventsApp/home.html', {'servicios': servicios})

def events(request):
    # Obtener todos los eventos, ordenados por fecha descendente
    eventos = Evento.objects.all().order_by('-fecha')
    
    # Pasar los eventos al contexto de la plantilla
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
    # Obtener miembros del equipo por categoría
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
    servicios_list = Servicio.objects.filter(activo=True)
    return render(request, 'eventsApp/servicios.html', {'servicios': servicios_list})