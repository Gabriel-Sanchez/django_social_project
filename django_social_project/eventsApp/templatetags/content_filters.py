from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()

@register.filter
def youtube_embed(value):
    """
    Convierte enlaces de YouTube en embeds seguros y responsivos
    Solo procesa URLs que NO están ya dentro de iframes o elementos media
    """
    if not value:
        return value
    
    # No procesar si ya contiene elementos media de CKEditor o iframes
    if '<figure class="media">' in value or 'data-oembed-url' in value:
        return value
    
    # Patrones para diferentes formatos de URL de YouTube (solo URLs sueltas)
    youtube_patterns = [
        r'(?<!src=")(?<!href=")https?://(?:www\.)?youtube\.com/watch\?v=([a-zA-Z0-9_-]+)(?![^<]*</iframe>)',
        r'(?<!src=")(?<!href=")https?://youtu\.be/([a-zA-Z0-9_-]+)(?![^<]*</iframe>)',
    ]
    
    # Procesar cada patrón
    for pattern in youtube_patterns:
        def replace_youtube(match):
            video_id = match.group(1)
            embed_html = f'''
            <div class="youtube-embed-container" style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; margin: 1.5em 0;">
                <iframe 
                    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
                    src="https://www.youtube.com/embed/{video_id}?rel=0&modestbranding=1"
                    title="Video de YouTube"
                    frameborder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowfullscreen>
                </iframe>
            </div>
            '''
            return embed_html
        
        value = re.sub(pattern, replace_youtube, value)
    
    return mark_safe(value)

@register.filter
def process_embeds(value):
    """
    Procesa diferentes tipos de embeds en el contenido
    """
    if not value:
        return value
    
    # Procesar YouTube
    value = youtube_embed(value)
    
    # Procesar otros embeds si es necesario (Vimeo, etc.)
    # value = vimeo_embed(value)
    
    return mark_safe(value)

@register.filter
def clean_ckeditor_media(value):
    """
    Limpia y mejora los elementos media generados por CKEditor
    """
    if not value:
        return value
    
    # Patrón más específico para limpiar el HTML malformado
    # Buscar elementos figure con data-oembed-url
    media_pattern = r'<figure class="media">[^<]*<div[^>]*data-oembed-url="[^"]*youtube\.com/embed/([a-zA-Z0-9_-]+)[^"]*"[^>]*>.*?</figure>'
    
    def clean_media_embed(match):
        video_id = match.group(1)
        return f'''<div class="youtube-embed-container">
    <iframe 
        src="https://www.youtube.com/embed/{video_id}?rel=0&modestbranding=1"
        title="Video de YouTube"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
    </iframe>
</div>'''
    
    # Aplicar limpieza
    value = re.sub(media_pattern, clean_media_embed, value, flags=re.DOTALL)
    
    # También limpiar cualquier iframe duplicado o malformado dentro de iframes
    value = re.sub(r'<iframe[^>]*src="[^"]*<div class="youtube-embed-container"[^"]*"[^>]*>.*?</iframe>', '', value, flags=re.DOTALL)
    
    # Limpiar atributos HTML malformados
    value = re.sub(r'youtube-embed-container"="', 'youtube-embed-container"', value)
    value = re.sub(r'allowfullscreen=""', 'allowfullscreen', value)
    
    return mark_safe(value)

@register.filter
def safe_content(value):
    """
    Renderiza contenido HTML de forma segura con estilos específicos
    """
    if not value:
        return value
    
    # Limpiar elementos media de CKEditor primero
    value = clean_ckeditor_media(value)
    
    # Procesar embeds para URLs sueltas
    value = process_embeds(value)
    
    # Agregar clases CSS a elementos específicos
    value = re.sub(r'<img([^>]*)>', r'<img\1 class="content-image">', value)
    value = re.sub(r'<table([^>]*)>', r'<table\1 class="content-table">', value)
    value = re.sub(r'<blockquote([^>]*)>', r'<blockquote\1 class="content-blockquote">', value)
    
    return mark_safe(value)

@register.filter
def extract_video_id(url):
    """
    Extrae el ID de video de una URL de YouTube
    """
    patterns = [
        r'(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)([a-zA-Z0-9_-]+)',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    return None 