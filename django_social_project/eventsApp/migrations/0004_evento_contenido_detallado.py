# Generated by Django 5.1.4 on 2025-04-20 00:33

from django_ckeditor_5.fields import CKEditor5Field
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventsApp', '0003_servicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='contenido_detallado',
            field=CKEditor5Field(blank=True, null=True, verbose_name='Contenido Detallado', config_name='extends'),
        ),
    ]
