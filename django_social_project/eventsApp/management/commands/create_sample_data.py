from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime, timedelta
from eventsApp.models import Evento, TeamMember

class Command(BaseCommand):
    help = 'Crea datos de ejemplo para la aplicación'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creando datos de ejemplo...')

        # Crear eventos
        eventos_data = [
            {
                'titulo': 'Misa Solemne de Domingo',
                'descripcion': 'Santa Misa dominical con coro parroquial.',
                'fecha': timezone.now() + timedelta(days=2),
                'lugar': 'Altar Principal',
            },
            {
                'titulo': 'Retiro Espiritual',
                'descripcion': 'Retiro espiritual para jóvenes. Tema: "Encuentro con Cristo".',
                'fecha': timezone.now() + timedelta(days=7),
                'lugar': 'Salón Parroquial',
            },
            {
                'titulo': 'Primera Comunión',
                'descripcion': 'Ceremonia de Primera Comunión para niños de catequesis.',
                'fecha': timezone.now() + timedelta(days=14),
                'lugar': 'Altar Principal',
            },
            {
                'titulo': 'Adoración al Santísimo',
                'descripcion': 'Hora Santa y adoración eucarística.',
                'fecha': timezone.now() + timedelta(days=1),
                'lugar': 'Capilla de Adoración',
            },
            {
                'titulo': 'Confirmaciones',
                'descripcion': 'Ceremonia de Confirmación presidida por el Obispo.',
                'fecha': timezone.now() + timedelta(days=21),
                'lugar': 'Altar Principal',
            }
        ]

        for evento_data in eventos_data:
            Evento.objects.create(**evento_data)
            self.stdout.write(f'Evento creado: {evento_data["titulo"]}')

        # Crear miembros del equipo pastoral
        team_members_data = [
            {
                'nombre': 'P. Juan Pablo Rodríguez',
                'rol': 'sacerdote',
                'descripcion': 'Párroco. Ordenado en 2005, dedicado especialmente a la pastoral juvenil y familiar.',
                'orden': 1,
                'activo': True,
            },
            {
                'nombre': 'P. Miguel Ángel Torres',
                'rol': 'sacerdote',
                'descripcion': 'Vicario Parroquial. Especialista en liturgia y música sacra.',
                'orden': 2,
                'activo': True,
            },
            {
                'nombre': 'Diác. Roberto Martínez',
                'rol': 'diacono',
                'descripcion': 'Diácono permanente. Coordina la pastoral social y el ministerio de visita a enfermos.',
                'orden': 3,
                'activo': True,
            },
            {
                'nombre': 'Diác. Carlos Sánchez',
                'rol': 'diacono',
                'descripcion': 'Diácono permanente. Encargado de la preparación pre-matrimonial y bautismal.',
                'orden': 4,
                'activo': True,
            },
            {
                'nombre': 'Ana María López',
                'rol': 'administrativo',
                'descripcion': 'Secretaria parroquial. Coordina las actividades administrativas y la atención al público.',
                'orden': 5,
                'activo': True,
            },
            {
                'nombre': 'Pedro Ramírez',
                'rol': 'administrativo',
                'descripcion': 'Coordinador de mantenimiento y logística de la parroquia.',
                'orden': 6,
                'activo': True,
            }
        ]

        for member_data in team_members_data:
            TeamMember.objects.create(**member_data)
            self.stdout.write(f'Miembro del equipo creado: {member_data["nombre"]}')

        self.stdout.write(self.style.SUCCESS('Datos de ejemplo creados exitosamente')) 