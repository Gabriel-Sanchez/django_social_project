# Generated by Django 5.1.4 on 2025-06-22 23:47

import django_ckeditor_5.fields
import eventsApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventsApp', '0008_alter_carouselimage_imagen_alter_teammember_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('resumen', models.TextField(help_text='Resumen corto de la noticia (máximo 300 caracteres)', max_length=300, verbose_name='Resumen')),
                ('contenido', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Contenido')),
                ('imagen', models.ImageField(blank=True, help_text='Imagen principal de la noticia. Máximo 2MB. Formato recomendado: JPG o PNG', null=True, upload_to='noticias/', validators=[eventsApp.models.validate_carousel_image_size])),
                ('autor', models.CharField(default='PROCLADEPAN', max_length=100, verbose_name='Autor')),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Publicación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Última Actualización')),
                ('activo', models.BooleanField(default=True, verbose_name='Publicado')),
                ('destacada', models.BooleanField(default=False, help_text='Marcar si es una noticia destacada')),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
                'ordering': ['-fecha_publicacion'],
            },
        ),
    ]
