# Generated by Django 5.1.4 on 2025-01-05 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateTimeField()),
                ('lugar', models.CharField(max_length=200)),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
