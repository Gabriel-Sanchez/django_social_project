from django.shortcuts import render
from django.http import HttpResponse
from .models import Contacto
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import logging

# Configurar el logger
logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'home/home.html')

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')

        print(f"\n=========== DATOS DEL FORMULARIO ==========")
        print(f"Nombre: {nombre}")
        print(f"Correo: {correo}")
        print(f"Asunto: {asunto}")
        print(f"Mensaje: {mensaje}")
        print(f"==========================================\n")

        # Guardar los datos en el modelo Contacto
        contacto = Contacto.objects.create(
            nombre=nombre,
            correo=correo,
            asunto=asunto,
            mensaje=mensaje
        )
        print("Datos guardados en la base de datos correctamente")

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

        return render(request, 'home/contacto.html')
    
    return render(request, 'home/contacto.html')