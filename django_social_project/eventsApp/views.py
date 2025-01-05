from django.shortcuts import render

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