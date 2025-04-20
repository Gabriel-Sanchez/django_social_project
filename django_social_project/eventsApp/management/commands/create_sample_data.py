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
                'titulo': 'Taller de Emprendimiento',
                'descripcion': 'Aprende las bases para iniciar tu propio negocio.',
                'contenido_detallado': """
                    <h2 style="color: #513b2a; margin-bottom: 1rem;">Taller de Emprendimiento: Tu Camino al Éxito</h2>
                    
                    <p class="mb-4">Te invitamos a participar en nuestro taller intensivo de emprendimiento, donde aprenderás las herramientas fundamentales para convertir tu idea en un negocio exitoso.</p>
                    
                    <h3 style="color: #513b2a; margin: 1rem 0;">¿Qué aprenderás?</h3>
                    <ul style="list-style-type: disc; margin-left: 1.5rem; margin-bottom: 1rem;">
                        <li>Desarrollo de modelo de negocio</li>
                        <li>Análisis de mercado</li>
                        <li>Estrategias de marketing digital</li>
                        <li>Gestión financiera básica</li>
                        <li>Plan de acción comercial</li>
                    </ul>

                    <h3 style="color: #513b2a; margin: 1rem 0;">Programa del Taller</h3>
                    <table style="width: 100%; margin-bottom: 1rem; border-collapse: collapse;">
                        <tr style="background-color: #f3f4f6;">
                            <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">Horario</th>
                            <th style="padding: 0.5rem; border: 1px solid #e5e7eb;">Actividad</th>
                        </tr>
                        <tr>
                            <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">9:00 - 10:30</td>
                            <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">Introducción al Emprendimiento</td>
                        </tr>
                        <tr>
                            <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">10:45 - 12:15</td>
                            <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">Modelo de Negocio Canvas</td>
                        </tr>
                        <tr>
                            <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">12:15 - 13:00</td>
                            <td style="padding: 0.5rem; border: 1px solid #e5e7eb;">Almuerzo</td>
                        </tr>
                    </table>

                    <div style="background-color: #f3f4f6; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0;">
                        <h4 style="color: #513b2a; margin-bottom: 0.5rem;">Requisitos:</h4>
                        <p>Traer una libreta, lápiz y muchas ganas de aprender. Si tienes una idea de negocio, ¡mejor aún!</p>
                    </div>
                """,
                'fecha': timezone.now() + timedelta(days=7),
                'lugar': 'Sala de Capacitación Principal'
            },
            {
                'titulo': 'Feria de Emprendedores',
                'descripcion': 'Exposición de productos y servicios de emprendedores locales.',
                'contenido_detallado': """
                    <h2 style="color: #513b2a; margin-bottom: 1rem;">Gran Feria de Emprendedores 2024</h2>

                    <div style="background-color: #513b2a; color: white; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
                        <p style="font-size: 1.1rem; font-weight: bold;">¡No te pierdas la oportunidad de mostrar tus productos y conectar con otros emprendedores!</p>
                    </div>

                    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-bottom: 1rem;">
                        <div style="background-color: #f3f4f6; padding: 1rem; border-radius: 0.5rem;">
                            <h4 style="color: #513b2a; margin-bottom: 0.5rem;">Para Expositores</h4>
                            <ul style="list-style-type: none;">
                                <li>✓ Stand completamente equipado</li>
                                <li>✓ Promoción en redes sociales</li>
                                <li>✓ Networking con otros emprendedores</li>
                            </ul>
                        </div>
                        <div style="background-color: #f3f4f6; padding: 1rem; border-radius: 0.5rem;">
                            <h4 style="color: #513b2a; margin-bottom: 0.5rem;">Para Visitantes</h4>
                            <ul style="list-style-type: none;">
                                <li>✓ Entrada gratuita</li>
                                <li>✓ Productos locales</li>
                                <li>✓ Talleres gratuitos</li>
                            </ul>
                        </div>
                    </div>

                    <h3 style="color: #513b2a; margin: 1rem 0;">Actividades Especiales</h3>
                    <ul style="list-style-type: disc; margin-left: 1.5rem; margin-bottom: 1rem;">
                        <li>Charlas de emprendedores exitosos</li>
                        <li>Demostraciones de productos</li>
                        <li>Networking coffee break</li>
                        <li>Rifa de productos de expositores</li>
                    </ul>

                    <div style="border: 2px solid #513b2a; padding: 1rem; border-radius: 0.5rem; margin-top: 1rem;">
                        <h4 style="color: #513b2a; margin-bottom: 0.5rem;">¿Quieres ser expositor?</h4>
                        <p>Inscripciones abiertas hasta el 15 de marzo. Cupos limitados.</p>
                    </div>
                """,
                'fecha': timezone.now() + timedelta(days=14),
                'lugar': 'Plaza Principal'
            },
            {
                'titulo': 'Curso de Panadería Básica',
                'descripcion': 'Aprende las técnicas fundamentales de la panadería.',
                'contenido_detallado': """
                    <h2 style="color: #513b2a; margin-bottom: 1rem;">Curso Intensivo de Panadería Básica</h2>

                    <p style="margin-bottom: 1rem;">Descubre el arte de la panadería en este curso práctico donde aprenderás las técnicas fundamentales para hacer pan artesanal de calidad profesional.</p>

                    <h3 style="color: #513b2a; margin: 1rem 0;">Contenido del Curso</h3>
                    <div style="background-color: #f3f4f6; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
                        <ol style="list-style-type: decimal; margin-left: 1.5rem;">
                            <li>Introducción a la panadería
                                <ul style="list-style-type: disc; margin-left: 1.5rem;">
                                    <li>Tipos de harinas</li>
                                    <li>Levaduras y fermentación</li>
                                    <li>Equipos básicos</li>
                                </ul>
                            </li>
                            <li>Técnicas básicas
                                <ul style="list-style-type: disc; margin-left: 1.5rem;">
                                    <li>Amasado manual</li>
                                    <li>Control de temperatura</li>
                                    <li>Tiempos de reposo</li>
                                </ul>
                            </li>
                            <li>Recetas prácticas
                                <ul style="list-style-type: disc; margin-left: 1.5rem;">
                                    <li>Pan blanco tradicional</li>
                                    <li>Pan integral</li>
                                    <li>Bollos dulces</li>
                                </ul>
                            </li>
                        </ol>
                    </div>

                    <div style="display: flex; gap: 1rem; margin-bottom: 1rem;">
                        <div style="flex: 1; background-color: #513b2a; color: white; padding: 1rem; border-radius: 0.5rem;">
                            <h4 style="margin-bottom: 0.5rem;">Duración</h4>
                            <p>4 sesiones de 3 horas</p>
                        </div>
                        <div style="flex: 1; background-color: #513b2a; color: white; padding: 1rem; border-radius: 0.5rem;">
                            <h4 style="margin-bottom: 0.5rem;">Incluye</h4>
                            <p>Materiales y recetario</p>
                        </div>
                    </div>

                    <div style="border: 2px dashed #513b2a; padding: 1rem; border-radius: 0.5rem;">
                        <h4 style="color: #513b2a; margin-bottom: 0.5rem;">Nota Importante</h4>
                        <p>Cupo limitado a 15 participantes para garantizar atención personalizada.</p>
                    </div>
                """,
                'fecha': timezone.now() + timedelta(days=21),
                'lugar': 'Taller de Panadería'
            }
        ]

        for evento_data in eventos_data:
            evento, created = Evento.objects.get_or_create(
                titulo=evento_data['titulo'],
                defaults={
                    'descripcion': evento_data['descripcion'],
                    'contenido_detallado': evento_data['contenido_detallado'],
                    'fecha': evento_data['fecha'],
                    'lugar': evento_data['lugar']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Evento creado: {evento.titulo}'))
            else:
                self.stdout.write(self.style.WARNING(f'Evento ya existe: {evento.titulo}'))

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