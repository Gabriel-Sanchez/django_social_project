from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.admin.views.decorators import staff_member_required
from django.core.files.storage import default_storage
from django.conf import settings
from django.core.exceptions import ValidationError
from .validators import validate_ckeditor_image
import os
import uuid
from datetime import datetime

@csrf_exempt
@require_POST
@staff_member_required
def ckeditor_upload(request):
    """
    Vista personalizada para subir imágenes a CKEditor con validación
    """
    if 'upload' not in request.FILES:
        return JsonResponse({
            'error': {
                'message': 'No se encontró ningún archivo para subir.'
            }
        }, status=400)
    
    upload_file = request.FILES['upload']
    
    try:
        # Validar la imagen usando nuestros validadores personalizados
        validate_ckeditor_image(upload_file)
        
        # Generar nombre único para el archivo
        file_extension = os.path.splitext(upload_file.name)[1].lower()
        unique_filename = f"{uuid.uuid4().hex}{file_extension}"
        
        # Crear estructura de carpetas por fecha
        now = datetime.now()
        upload_path = os.path.join(
            settings.CKEDITOR_5_UPLOAD_PATH,
            str(now.year),
            f"{now.month:02d}"
        )
        
        # Ruta completa del archivo
        file_path = os.path.join(upload_path, unique_filename)
        
        # Guardar el archivo
        saved_path = default_storage.save(file_path, upload_file)
        file_url = default_storage.url(saved_path)
        
        # Respuesta exitosa para CKEditor
        return JsonResponse({
            'url': file_url,
            'uploaded': True
        })
        
    except ValidationError as e:
        return JsonResponse({
            'error': {
                'message': str(e.message) if hasattr(e, 'message') else str(e)
            }
        }, status=400)
    
    except Exception as e:
        return JsonResponse({
            'error': {
                'message': f'Error al subir el archivo: {str(e)}'
            }
        }, status=500)

@csrf_exempt
@require_POST  
@staff_member_required
def ckeditor_browse(request):
    """
    Vista para navegar archivos subidos (opcional)
    """
    try:
        upload_path = os.path.join(settings.MEDIA_ROOT, settings.CKEDITOR_5_UPLOAD_PATH)
        files = []
        
        if os.path.exists(upload_path):
            for root, dirs, filenames in os.walk(upload_path):
                for filename in filenames:
                    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')):
                        file_path = os.path.join(root, filename)
                        rel_path = os.path.relpath(file_path, settings.MEDIA_ROOT)
                        file_url = settings.MEDIA_URL + rel_path.replace('\\', '/')
                        
                        files.append({
                            'name': filename,
                            'url': file_url,
                            'size': os.path.getsize(file_path)
                        })
        
        return JsonResponse({
            'files': files
        })
        
    except Exception as e:
        return JsonResponse({
            'error': {
                'message': f'Error al listar archivos: {str(e)}'
            }
        }, status=500) 