from django.http import JsonResponse
from django.core.exceptions import ValidationError
from .validators import validate_ckeditor_image
import json

class CKEditorUploadMiddleware:
    """
    Middleware para interceptar y validar todas las subidas de archivos de CKEditor,
    incluyendo las que se hacen por drag & drop
    """
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Interceptar requests de subida de CKEditor
        if (request.method == 'POST' and 
            request.path.startswith('/ckeditor5/') and 
            'upload' in request.FILES):
            
            return self.validate_ckeditor_upload(request)
        
        response = self.get_response(request)
        return response

    def validate_ckeditor_upload(self, request):
        """
        Valida las subidas de CKEditor antes de procesarlas
        """
        try:
            upload_file = request.FILES.get('upload')
            if upload_file:
                # Aplicar nuestras validaciones personalizadas
                validate_ckeditor_image(upload_file)
                
                # Si pasa las validaciones, continuar con el procesamiento normal
                response = self.get_response(request)
                return response
            else:
                return JsonResponse({
                    'error': {
                        'message': 'No se encontró ningún archivo para subir.'
                    }
                }, status=400)
                
        except ValidationError as e:
            # Devolver error de validación en formato CKEditor
            return JsonResponse({
                'error': {
                    'message': str(e.message) if hasattr(e, 'message') else str(e)
                }
            }, status=400)
        except Exception as e:
            return JsonResponse({
                'error': {
                    'message': f'Error al validar el archivo: {str(e)}'
                }
            }, status=500)

class FileSizeMiddleware:
    """
    Middleware adicional para validar el tamaño de archivos a nivel global
    """
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'POST' and request.FILES:
            # Verificar tamaño de todos los archivos subidos
            for field_name, uploaded_file in request.FILES.items():
                if uploaded_file.size > 2 * 1024 * 1024:  # 2MB (más estricto)
                    if 'ckeditor' in request.path.lower() or 'upload' in field_name.lower():
                        return JsonResponse({
                            'error': {
                                'message': f'El archivo "{uploaded_file.name}" es demasiado grande. '
                                         f'Tamaño máximo permitido: 2MB. '
                                         f'Tu archivo pesa: {uploaded_file.size / (1024 * 1024):.1f}MB'
                            }
                        }, status=400)

        response = self.get_response(request)
        return response 