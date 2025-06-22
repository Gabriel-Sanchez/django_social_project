from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Evento, TeamMember, Servicio, CarouselImage, About
from django.utils import timezone
from datetime import timedelta
from django.core.paginator import Paginator
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def get_upcoming_events(limit=3):
    now = timezone.now()
    return Evento.objects.filter(fecha__gte=now).order_by('fecha')[:limit]

def home(request):
    # Get active carousel images
    carousel_images = CarouselImage.objects.filter(activo=True)
    
    # Get upcoming events (existing code)
    eventos_proximos = Evento.objects.filter(
        fecha__gte=timezone.now()
    ).order_by('fecha')[:3]
    
    # Get active services (existing code)
    servicios = Servicio.objects.filter(activo=True).order_by('orden')
    
    context = {
        'carousel_images': carousel_images,
        'eventos_proximos': eventos_proximos,
        'servicios': servicios,
    }
    return render(request, 'eventsApp/home.html', context)

def events(request):
    eventos_list = Evento.objects.all().order_by('-fecha')
    paginator = Paginator(eventos_list, 10)  # 10 eventos por página
    
    page_number = request.GET.get('page', 1)
    eventos = paginator.get_page(page_number)
    
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

def mision_vision_valores(request):
    about = About.objects.filter(activo=True).first()
    context = {
        'about': about,
    }
    return render(request, 'eventsApp/mision_vision_valores.html', context)

def ubicacion(request):
    return render(request, 'eventsApp/ubicacion.html')

def equipo_pastoral(request):
    sacerdotes = TeamMember.objects.filter(rol='sacerdote', activo=True)
    diaconos = TeamMember.objects.filter(rol='diacono', activo=True)
    administrativos = TeamMember.objects.filter(rol='administrativo', activo=True)
    
    context = {
        'sacerdotes': sacerdotes,
        'diaconos': diaconos,
        'administrativos': administrativos,
    }
    return render(request, 'eventsApp/equipo_pastoral.html', context)

def historia(request):
    about = About.objects.filter(activo=True).first()
    context = {
        'about': about,
    }
    return render(request, 'eventsApp/historia.html', context)

def fundaciones_hermanas(request):
    return render(request, 'eventsApp/fundaciones_hermanas.html')

def donaciones(request):
    return render(request, 'eventsApp/donaciones.html')

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('email')  # Note: the form uses 'email' not 'correo'
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')

        print(f"\n=========== DATOS DEL FORMULARIO ==========")
        print(f"Nombre: {nombre}")
        print(f"Correo: {correo}")
        print(f"Asunto: {asunto}")
        print(f"Mensaje: {mensaje}")
        print(f"==========================================\n")

        try:
            # Verificar configuración de correo
            print("\n=== CONFIGURACIÓN DE CORREO ===")
            print(f"EMAIL_BACKEND: {settings.EMAIL_BACKEND}")
            print(f"EMAIL_HOST: {settings.EMAIL_HOST}")
            print(f"EMAIL_PORT: {settings.EMAIL_PORT}")
            print(f"EMAIL_USE_TLS: {settings.EMAIL_USE_TLS}")
            print(f"EMAIL_HOST_USER: {settings.EMAIL_HOST_USER}")
            print(f"ADMIN_EMAIL: {settings.ADMIN_EMAIL}")
            print("=============================\n")
            
            # Preparar el mensaje
            email_subject = f'Nuevo mensaje de contacto: {asunto}'
            email_body = f'''
            Has recibido un nuevo mensaje de contacto:

            Nombre: {nombre}
            Correo: {correo}
            Asunto: {asunto}
            Mensaje: {mensaje}

            Puedes responder este mensaje directamente a {correo}
            '''
            
            print("Intentando enviar correo...")
            # Usar el método send_mail de Django
            send_mail(
                subject=email_subject,
                message=email_body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=False,
            )
            print("Correo enviado exitosamente.")
            
            # Mensaje de éxito
            messages.success(request, f'''
                ¡Gracias por contactarnos, {nombre}!
                Tu mensaje ha sido enviado correctamente.
                Nos pondremos en contacto contigo a la brevedad posible.
            ''')
            
        except Exception as e:
            print(f"\n### ERROR AL ENVIAR CORREO: {str(e)} ###")
            print(f"Tipo de error: {type(e).__name__}\n")
            messages.error(request, f'''
                Hubo un error al enviar tu mensaje: {str(e)}
                Por favor, intenta nuevamente más tarde o contáctanos directamente a nuestro correo electrónico.
            ''')

    return render(request, 'eventsApp/contacto.html')

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
            'id': evento.id,
            'title': evento.titulo,
            'start': evento.fecha.isoformat(),
            'description': evento.descripcion,
            'location': evento.lugar
        })
    return JsonResponse(data, safe=False)

def event_detail(request, event_id):
    evento = get_object_or_404(Evento, id=event_id)
    context = {
        'evento': evento,
    }
    return render(request, 'eventsApp/event_detail.html', context)

def cooperacion(request):
    return render(request, 'eventsApp/que_hacemos/cooperacion.html')

def ayuda_humanitaria(request):
    return render(request, 'eventsApp/que_hacemos/ayuda_humanitaria.html')

def accion_social(request):
    return render(request, 'eventsApp/que_hacemos/accion_social.html')

def educacion_sensibilizacion(request):
    return render(request, 'eventsApp/que_hacemos/educacion_sensibilizacion.html')

def comercio_justo(request):
    return render(request, 'eventsApp/que_hacemos/comercio_justo.html')