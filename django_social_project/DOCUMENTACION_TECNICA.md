# Documentación Técnica - Django Social Project

## Índice
1. [Resumen del Proyecto](#resumen-del-proyecto)
2. [Arquitectura del Sistema](#arquitectura-del-sistema)
3. [Configuración del Entorno](#configuración-del-entorno)
4. [Estructura de Aplicaciones](#estructura-de-aplicaciones)
5. [Modelos de Datos](#modelos-de-datos)
6. [Vistas y URLs](#vistas-y-urls)
7. [Middleware y Validaciones](#middleware-y-validaciones)
8. [Configuración de CKEditor](#configuración-de-ckeditor)
9. [Sistema de Correo Electrónico](#sistema-de-correo-electrónico)
10. [Comandos de Administración](#comandos-de-administración)
11. [Estructura de Templates](#estructura-de-templates)
12. [Recomendaciones de Mejora](#recomendaciones-de-mejora)

---

## Resumen del Proyecto

**Django Social Project** es una aplicación web desarrollada en Django para una organización social/religiosa (PROCLADEPAN). El sistema gestiona:

- **Eventos**: Administración de eventos comunitarios con contenido detallado
- **Noticias**: Sistema de publicación de noticias con paginación
- **Equipo Pastoral**: Gestión de miembros del equipo (sacerdotes, diáconos, personal administrativo)
- **Servicios**: Catálogo de servicios ofrecidos por la organización
- **Información Institucional**: Misión, visión, valores e historia
- **Contacto**: Sistema de contacto con envío de correos electrónicos
- **Carrusel de Imágenes**: Gestión de imágenes destacadas en la página principal

### Tecnologías Utilizadas
- **Django 5.1.4**
- **SQLite** (base de datos)
- **CKEditor 5** (editor de texto enriquecido)
- **Python dotenv** (gestión de variables de entorno)
- **Django middleware personalizado** (validaciones de archivos)

---

## Arquitectura del Sistema

### Estructura de Aplicaciones Django

```
django_social_project/
├── django_social_project/     # Configuración principal
├── base/                      # App base con templates generales
├── home/                      # App para páginas de inicio y contacto
├── eventsApp/                 # App principal con la mayoría de funcionalidades
├── static/                    # Archivos estáticos globales
├── media/                     # Archivos subidos por usuarios
└── manage.py                  # Archivo de administración Django
```

### Patrón MVT (Model-View-Template)
El proyecto sigue el patrón MVT estándar de Django:
- **Models**: Definición de estructura de datos
- **Views**: Lógica de negocio y procesamiento de requests
- **Templates**: Presentación y interfaz de usuario

---

## Configuración del Entorno

### Variables de Entorno (archivo .env)
```bash
# Configuración de Debug
DEBUG=True

# Hosts permitidos (separados por comas)
ALLOWED_HOSTS=localhost,127.0.0.1,tu-dominio.com

# Configuración de correo electrónico
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=tu-email@gmail.com
EMAIL_HOST_PASSWORD=tu-contraseña-app
ADMIN_EMAIL=admin@tu-organizacion.com
```

### Configuración de Base de Datos
- **Motor**: SQLite (desarrollo)
- **Archivo**: `db.sqlite3`
- **Ubicación**: Raíz del proyecto

### Configuración de Archivos Estáticos
- **STATIC_URL**: `/static/`
- **STATIC_ROOT**: `staticfiles/`
- **MEDIA_URL**: `/media/`
- **MEDIA_ROOT**: `media/`

---

## Estructura de Aplicaciones

### 1. App `base`
**Propósito**: Plantillas base y funcionalidades generales
- **Models**: Vacío
- **Views**: Funciones básicas
- **Templates**: `base.html`, `servicios.html`

### 2. App `home`
**Propósito**: Página de inicio y contacto simple
- **Models**: `Contacto` (formulario de contacto)
- **Views**: `home`, `contacto`
- **Templates**: `home.html`, `contacto.html`

### 3. App `eventsApp` (Principal)
**Propósito**: Funcionalidades principales del sistema
- **Models**: `Evento`, `TeamMember`, `Servicio`, `CarouselImage`, `About`, `Noticia`
- **Views**: 20+ vistas para diferentes funcionalidades
- **Templates**: Amplia variedad de plantillas organizadas por funcionalidad

---

## Modelos de Datos

### Modelo `Evento`
```python
class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    lugar = models.CharField(max_length=200)
    creado_en = models.DateTimeField(auto_now_add=True)
    contenido_detallado = CKEditor5Field(blank=True, null=True)
```
**Funcionalidades**:
- Listado con paginación
- Vista detallada individual
- API JSON para calendario
- Contenido enriquecido con CKEditor

### Modelo `TeamMember`
```python
class TeamMember(models.Model):
    ROL_CHOICES = [
        ('sacerdote', 'Sacerdote'),
        ('diacono', 'Diácono'),
        ('administrativo', 'Personal Administrativo'),
    ]
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='team/', validators=[validate_team_image_size])
    orden = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
```
**Funcionalidades**:
- Clasificación por roles
- Validación de tamaño de imágenes (máx. 1MB)
- Ordenamiento personalizable
- Estado activo/inactivo

### Modelo `Servicio`
```python
class Servicio(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    requisitos = models.TextField()
    horario = models.CharField(max_length=200, blank=True)
    contacto = models.CharField(max_length=200, blank=True)
    orden = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
```

### Modelo `CarouselImage`
```python
class CarouselImage(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='carousel/', validators=[validate_carousel_image_size])
    orden = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
```
**Funcionalidades**:
- Validación de tamaño de imágenes (máx. 2MB)
- Ordenamiento personalizable
- Títulos y subtítulos

### Modelo `Noticia`
```python
class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    resumen = models.TextField(max_length=300)
    contenido = CKEditor5Field(config_name='extends')
    imagen = models.ImageField(upload_to='noticias/', validators=[validate_carousel_image_size])
    autor = models.CharField(max_length=100, default="PROCLADEPAN")
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    destacada = models.BooleanField(default=False)
```
**Funcionalidades**:
- Contenido enriquecido con CKEditor
- Sistema de autor
- Noticias destacadas
- Paginación (6 por página)

### Modelo `About`
```python
class About(models.Model):
    objetivo = CKEditor5Field(config_name='extends')
    mision = CKEditor5Field(config_name='extends')
    vision = CKEditor5Field(config_name='extends')
    historia = CKEditor5Field(config_name='extends')
    activo = models.BooleanField(default=True)
```
**Funcionalidades**:
- Solo un registro activo permitido
- Contenido enriquecido para cada sección
- Automáticamente desactiva otros registros al activar uno

---

## Vistas y URLs

### Estructura de URLs Principal
```python
# django_social_project/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('', include('eventsApp.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]
```

### URLs de eventsApp
```python
# eventsApp/urls.py
urlpatterns = [
    path('inicio/', views.home, name='inicio'),
    path('eventos/', views.events, name='events'),
    path('eventos/<int:event_id>/', views.event_detail, name='event_detail'),
    path('eventos/calendario/api/', views.eventos_calendario_api, name='eventos_calendario_api'),
    path('informacion/mision-vision-valores/', views.mision_vision_valores, name='mision_vision_valores'),
    path('informacion/equipo-pastoral/', views.equipo_pastoral, name='equipo_pastoral'),
    path('informacion/historia/', views.historia, name='historia'),
    path('contacto/', views.contacto, name='contacto'),
    path('servicios/', views.servicios, name='servicios'),
    path('noticias/', views.noticias, name='noticias'),
    path('noticias/<int:noticia_id>/', views.noticia_detail, name='noticia_detail'),
    path('ckeditor/upload/', ckeditor_views.ckeditor_upload, name='ckeditor_upload'),
    path('', views.home, name='index'),
]
```

### Vistas Principales

#### Vista `home`
- Obtiene imágenes activas del carrusel
- Muestra próximos 3 eventos
- Lista servicios activos
- Renderiza la página principal

#### Vista `events`
- Listado paginado de eventos (10 por página)
- Ordenado por fecha descendente
- Funcionalidad de búsqueda básica

#### Vista `contacto`
- Formulario POST para envío de mensajes
- Validación de datos
- Envío automático de correos electrónicos
- Manejo de errores con mensajes informativos

#### Vista `equipo_pastoral`
- Separa miembros por roles (sacerdotes, diáconos, administrativos)
- Solo muestra miembros activos
- Ordenado por campo `orden`

#### Vista `noticias`
- Listado paginado (6 por página)
- Solo noticias activas
- Ordenado por fecha de publicación descendente

---

## Middleware y Validaciones

### Middleware Personalizado

#### `FileSizeMiddleware`
- Valida tamaño de archivos a nivel global
- Límite: 2MB para todas las subidas
- Devuelve respuesta JSON para uploads de CKEditor

#### `CKEditorUploadMiddleware`
- Intercepta subidas específicas de CKEditor
- Aplica validaciones personalizadas
- Maneja errores de validación con formato JSON

### Validadores Personalizados

#### `validate_image_size`
- Límite: 2MB para imágenes
- Mensaje informativo con tamaño actual

#### `validate_image_dimensions`
- Límite: 2048x2048 píxeles
- Validación opcional (no bloquea si no se pueden obtener dimensiones)

#### `validate_image_format`
- Formatos permitidos: JPG, JPEG, PNG, GIF, BMP, WEBP
- Validación por extensión de archivo

#### `validate_ckeditor_image`
- Validador completo que combina formato, tamaño y dimensiones
- Específico para uploads de CKEditor

---

## Configuración de CKEditor

### Configuración Principal (`settings.py`)
```python
CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': ['heading', '|', 'bold', 'italic', 'link',
                   'bulletedList', 'numberedList', 'blockQuote', 'imageUpload'],
        'image': {
            'upload': {
                'types': ['jpeg', 'jpg', 'png', 'gif', 'bmp', 'webp'],
                'maxFileSize': '2MB'
            }
        }
    },
    'extends': {
        'toolbar': ['heading', '|', 'bold', 'italic', 'link', 'underline', 
                   'fontColor', 'fontBackgroundColor', 'insertTable', 'imageUpload'],
        'image': {
            'upload': {
                'types': ['jpeg', 'jpg', 'png', 'gif', 'bmp', 'webp'],
                'maxFileSize': '2MB'
            }
        }
    }
}
```

### Configuración de Subida
- **URL personalizada**: `/ckeditor/upload/`
- **Validación**: Mediante middleware y validadores personalizados
- **Tamaño máximo**: 2MB por archivo
- **Formatos**: JPG, PNG, GIF, BMP, WEBP

---

## Sistema de Correo Electrónico

### Configuración SMTP
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')
```

### Funcionalidad de Contacto
- **Formulario**: Nombre, email, asunto, mensaje
- **Validación**: Campos obligatorios
- **Envío**: Automático al email administrador
- **Respuesta**: Mensajes de éxito/error para el usuario
- **Logging**: Información detallada en consola para debugging

---

## Comandos de Administración

### Comando `create_sample_data`
**Ubicación**: `eventsApp/management/commands/create_sample_data.py`

**Funcionalidad**:
- Crea eventos de ejemplo con contenido detallado
- Genera miembros del equipo pastoral
- Datos realistas para testing y desarrollo

**Uso**:
```bash
python manage.py create_sample_data
```

**Datos que crea**:
- 3 eventos con contenido HTML detallado
- Miembros del equipo por roles
- Fechas futuras para eventos

---

## Estructura de Templates

### Organización de Templates
```
templates/
├── base/
│   ├── base.html              # Template base principal
│   └── servicios.html         # Template de servicios
├── home/
│   ├── home.html             # Página de inicio alternativa
│   └── contacto.html         # Formulario de contacto
└── eventsApp/
    ├── home.html             # Página principal
    ├── events.html           # Listado de eventos
    ├── event_detail.html     # Detalle de evento
    ├── noticias.html         # Listado de noticias
    ├── noticia_detail.html   # Detalle de noticia
    ├── equipo_pastoral.html  # Equipo pastoral
    ├── contacto.html         # Formulario de contacto
    ├── servicios.html        # Servicios ofrecidos
    └── que_hacemos/          # Subcarpeta de actividades
        ├── cooperacion.html
        ├── ayuda_humanitaria.html
        ├── accion_social.html
        ├── educacion_sensibilizacion.html
        └── comercio_justo.html
```

### Template Tags Personalizados
**Ubicación**: `eventsApp/templatetags/content_filters.py`
- Filtros para procesamiento de contenido
- Utilidades para templates

---

## Administración Django

### Configuración de Admin
**Ubicación**: `eventsApp/admin.py`

#### Admin de Eventos
- **Listado**: Título, fecha, lugar, fecha de creación
- **Búsqueda**: Por título, descripción, lugar
- **Filtros**: Por fecha y fecha de creación
- **Jerarquía**: Por fecha
- **Fieldsets**: Información básica y contenido detallado

#### Admin de Noticias
- **Listado**: Título, autor, fecha de publicación, estado activo
- **Búsqueda**: Por título y contenido
- **Filtros**: Por fecha de publicación, autor, estado
- **Acciones**: Activar/desactivar en lote

#### Admin de Equipo Pastoral
- **Listado**: Nombre, rol, estado activo
- **Búsqueda**: Por nombre y descripción
- **Filtros**: Por rol y estado
- **Ordenamiento**: Por orden y nombre

---

## Configuración de Seguridad

### Validaciones de Archivo
- **Tamaño máximo**: 2MB para imágenes
- **Formatos permitidos**: JPG, PNG, GIF, BMP, WEBP
- **Dimensiones máximas**: 2048x2048 píxeles
- **Validación a nivel**: Modelo, middleware y CKEditor

### Configuración de Subida
```python
DATA_UPLOAD_MAX_MEMORY_SIZE = 2 * 1024 * 1024  # 2MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 2 * 1024 * 1024  # 2MB
DATA_UPLOAD_MAX_NUMBER_FIELDS = 1000
DATA_UPLOAD_MAX_NUMBER_FILES = 20
```

### Middleware de Seguridad
- **CSRF Protection**: Activado
- **XFrame Options**: Protección contra clickjacking
- **Security Middleware**: Configuración estándar de Django

---

## Recomendaciones de Mejora

### 1. Base de Datos
- **Migrar a PostgreSQL**: Para producción
- **Backup automatizado**: Sistema de respaldos
- **Índices**: Optimizar consultas frecuentes

### 2. Seguridad
- **Autenticación**: Sistema de usuarios más robusto
- **Autorización**: Permisos granulares
- **HTTPS**: Configuración SSL/TLS
- **Variables de entorno**: Protección de SECRET_KEY

### 3. Performance
- **Cache**: Redis o Memcached
- **CDN**: Para archivos estáticos
- **Optimización de imágenes**: Redimensionamiento automático
- **Paginación**: Optimizar consultas con select_related

### 4. Funcionalidades
- **SEO**: Meta tags dinámicos
- **Sitemap**: Generación automática
- **RSS**: Feed de noticias
- **Búsqueda**: Sistema de búsqueda avanzada
- **Comentarios**: Sistema de comentarios en noticias

### 5. Monitoreo
- **Logging**: Sistema de logs estructurado
- **Métricas**: Monitoreo de performance
- **Alertas**: Notificaciones de errores
- **Analytics**: Integración con Google Analytics

### 6. Desarrollo
- **Tests**: Suite de pruebas unitarias
- **CI/CD**: Pipeline de integración continua
- **Docker**: Containerización para despliegue
- **Documentation**: Documentación de API

### 7. UI/UX
- **Responsive**: Mejorar experiencia móvil
- **Accesibilidad**: Cumplir estándares WCAG
- **Loading**: Indicadores de carga
- **Error pages**: Páginas de error personalizadas

---

## Instalación y Configuración

### Prerrequisitos
```bash
Python >= 3.8
Django >= 5.1
```

### Instalación
```bash
# Clonar repositorio
git clone <repository-url>
cd django_social_project

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tus configuraciones

# Ejecutar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Cargar datos de ejemplo (opcional)
python manage.py create_sample_data

# Ejecutar servidor
python manage.py runserver
```

### Configuración de Producción
```bash
# Configurar variables de entorno
DEBUG=False
ALLOWED_HOSTS=tu-dominio.com,www.tu-dominio.com

# Configurar servidor web (nginx + gunicorn)
pip install gunicorn
gunicorn django_social_project.wsgi:application

# Configurar archivos estáticos
python manage.py collectstatic
```

---

## Contacto y Soporte

Para cualquier duda o mejora del proyecto, contactar al equipo de desarrollo o revisar la documentación adicional en el repositorio.

**Última actualización**: Enero 2025
**Versión de Django**: 5.1.4
**Versión de Python**: 3.8+ 