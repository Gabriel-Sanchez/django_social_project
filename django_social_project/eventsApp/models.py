from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    lugar = models.CharField(max_length=200)
    creado_en = models.DateTimeField(auto_now_add=True)
    contenido_detallado = RichTextField(blank=True, null=True, verbose_name="Contenido Detallado")

    def get_absolute_url(self):
        return reverse('event_detail', args=[str(self.id)])

    def __str__(self):
        return self.titulo

class TeamMember(models.Model):
    ROL_CHOICES = [
        ('sacerdote', 'Sacerdote'),
        ('diacono', 'Diácono'),
        ('administrativo', 'Personal Administrativo'),
    ]
    
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='team/', blank=True, null=True)
    orden = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ['orden', 'nombre']

    def __str__(self):
        return f"{self.nombre} - {self.get_rol_display()}"

class Servicio(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    requisitos = models.TextField()
    horario = models.CharField(max_length=200, blank=True)
    contacto = models.CharField(max_length=200, blank=True)
    orden = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ['orden']
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return self.nombre

class CarouselImage(models.Model):
    titulo = models.CharField(max_length=100, help_text="Título que aparecerá sobre la imagen")
    subtitulo = models.CharField(max_length=200, help_text="Subtítulo o descripción corta")
    imagen = models.ImageField(upload_to='carousel/', help_text="Imagen para el carrusel (recomendado: 1920x1080px)")
    orden = models.IntegerField(default=0, help_text="Orden en que aparecerá la imagen (menor número = primero)")
    activo = models.BooleanField(default=True, help_text="Determina si la imagen se muestra en el carrusel")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['orden', '-fecha_creacion']
        verbose_name = "Imagen del Carrusel"
        verbose_name_plural = "Imágenes del Carrusel"

    def __str__(self):
        return self.titulo