from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from django.utils.translation import gettext_lazy as _
import os

def validate_image_size(image):
    """
    Valida el tamaño del archivo de imagen para CKEditor
    Límite: 2MB (reducido para ser más estricto)
    """
    max_size = 2 * 1024 * 1024  # 2MB en bytes (más estricto)
    
    if image.size > max_size:
        raise ValidationError(
            'El archivo es demasiado grande. El tamaño máximo permitido es 2MB. '
            'Tu archivo pesa {:.1f}MB.'.format(image.size / (1024 * 1024))
        )

def validate_image_dimensions(image):
    """
    Valida las dimensiones de la imagen
    Máximo: 2048x2048 píxeles
    """
    max_width = 2048
    max_height = 2048
    
    try:
        width, height = get_image_dimensions(image)
        if width and height:
            if width > max_width or height > max_height:
                raise ValidationError(
                    _('Las dimensiones de la imagen son demasiado grandes. '
                      'Máximo permitido: {}x{} píxeles. '
                      'Tu imagen: {}x{} píxeles.').format(
                        max_width, max_height, width, height
                    )
                )
    except Exception:
        # Si no se pueden obtener las dimensiones, permitir la subida
        pass

def validate_image_format(image):
    """
    Valida el formato del archivo de imagen
    """
    allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']
    
    ext = os.path.splitext(image.name)[1].lower()
    if ext not in allowed_extensions:
        raise ValidationError(
            _('Formato de archivo no permitido. '
              'Formatos permitidos: {}').format(', '.join(allowed_extensions))
        )

def validate_ckeditor_image(image):
    """
    Validador completo para imágenes de CKEditor
    """
    validate_image_format(image)
    validate_image_size(image)
    validate_image_dimensions(image) 