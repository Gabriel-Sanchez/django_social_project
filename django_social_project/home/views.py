from django.shortcuts import render
from django.http import HttpResponse
from .models import Contacto
from django.contrib import messages


def home(request):
    return render(request, 'home/home.html')



def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')

        # Guardar los datos en el modelo Contacto
        Contacto.objects.create(
            nombre=nombre,
            correo=correo,
            asunto=asunto,
            mensaje=mensaje
        )
        messages.success(request, "Gracias por contactarnos. Tu mensaje ha sido recibido.")
        return render(request, 'home/contacto.html')
    
    return render(request, 'home/contacto.html')