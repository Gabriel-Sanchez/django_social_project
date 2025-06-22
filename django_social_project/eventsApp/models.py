from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.urls import reverse
from django.core.exceptions import ValidationError

def validate_team_image_size(image):
    filesize = image.size
    megabyte_limit = 1.0
    if filesize > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"La imagen no puede ser mayor a {megabyte_limit}MB")

def validate_carousel_image_size(image):
    filesize = image.size
    megabyte_limit = 2.0
    if filesize > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"La imagen no puede ser mayor a {megabyte_limit}MB")

# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    lugar = models.CharField(max_length=200)
    creado_en = models.DateTimeField(auto_now_add=True)
    contenido_detallado = CKEditor5Field(blank=True, null=True, verbose_name="Contenido Detallado", config_name='extends')

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
    imagen = models.ImageField(
        upload_to='team/', 
        blank=True, 
        null=True,
        validators=[validate_team_image_size],
        help_text="Máximo 1MB. Formato recomendado: JPG o PNG"
    )
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
    imagen = models.ImageField(
        upload_to='carousel/', 
        help_text="Imagen para el carrusel (recomendado: 1920x1080px). Máximo 2MB. Formato recomendado: JPG",
        validators=[validate_carousel_image_size]
    )
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

class Noticia(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    resumen = models.TextField(max_length=300, verbose_name="Resumen", help_text="Resumen corto de la noticia (máximo 300 caracteres)")
    contenido = CKEditor5Field(verbose_name="Contenido", config_name='extends')
    imagen = models.ImageField(
        upload_to='noticias/', 
        blank=True, 
        null=True,
        validators=[validate_carousel_image_size],
        help_text="Imagen principal de la noticia. Máximo 2MB. Formato recomendado: JPG o PNG"
    )
    autor = models.CharField(max_length=100, default="PROCLADEPAN", verbose_name="Autor")
    fecha_publicacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Publicación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")
    activo = models.BooleanField(default=True, verbose_name="Publicado")
    destacada = models.BooleanField(default=False, help_text="Marcar si es una noticia destacada")

    class Meta:
        ordering = ['-fecha_publicacion']
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('noticia_detail', args=[str(self.id)])

class About(models.Model):
    objetivo = CKEditor5Field(verbose_name="Objetivo", config_name='extends')
    mision = CKEditor5Field(verbose_name="Misión", config_name='extends')
    vision = CKEditor5Field(verbose_name="Visión", config_name='extends')
    historia = CKEditor5Field(verbose_name="Historia", config_name='extends')
    activo = models.BooleanField(default=True, help_text="Solo debe haber un registro activo")
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Información Institucional"
        verbose_name_plural = "Información Institucional"

    def __str__(self):
        return "Información Institucional"

    def save(self, *args, **kwargs):
        if self.activo:
            # Desactivar otros registros activos
            About.objects.exclude(pk=self.pk).update(activo=False)
        super().save(*args, **kwargs)