from django.db import models

# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    lugar = models.CharField(max_length=200)
    creado_en = models.DateTimeField(auto_now_add=True)

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