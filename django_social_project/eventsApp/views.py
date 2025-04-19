from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


from .models import Evento

def events(request):
    # Obtener todos los eventos, ordenados por fecha descendente
    eventos = Evento.objects.all().order_by('-fecha')
    
    # Pasar los eventos al contexto de la plantilla
    context = {
        'eventos': eventos,
    }
    return render(request, 'eventsApp/events.html', context)

def get_calendar_events(request):
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