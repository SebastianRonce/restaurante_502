from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from gestion.models import Cliente, Empleado, Mesa, Plato, Orden, Factura


class Command(BaseCommand):
    help = 'Crea los grupos de roles y los usuarios del sistema'

    def handle(self, *args, **kwargs):

        # ── Permisos por modelo ──────────────────────────────
        def perms(model, acciones):
            ct = ContentType.objects.get_for_model(model)
            return [
                Permission.objects.get(content_type=ct, codename=f'{a}_{model._meta.model_name}')
                for a in acciones
            ]

        # ── GRUPO: Administrador ─────────────────────────────
        admin_group, _ = Group.objects.get_or_create(name='administrador')
        admin_perms = []
        for model in [Cliente, Empleado, Mesa, Plato, Orden, Factura]:
            admin_perms += perms(model, ['add', 'change', 'delete', 'view'])
        admin_group.permissions.set(admin_perms)
        self.stdout.write(self.style.SUCCESS('✓ Grupo administrador creado'))

        # ── GRUPO: Mesero ────────────────────────────────────
        mesero_group, _ = Group.objects.get_or_create(name='mesero')
        mesero_perms = (
            perms(Cliente, ['view']) +
            perms(Mesa,    ['view']) +
            perms(Plato,   ['view']) +
            perms(Orden,   ['add', 'change', 'view'])
        )
        mesero_group.permissions.set(mesero_perms)
        self.stdout.write(self.style.SUCCESS('✓ Grupo mesero creado'))

        # ── GRUPO: Cajero ────────────────────────────────────
        cajero_group, _ = Group.objects.get_or_create(name='cajero')
        cajero_perms = (
            perms(Orden,    ['view']) +
            perms(Factura,  ['add', 'view'])
        )
        cajero_group.permissions.set(cajero_perms)
        self.stdout.write(self.style.SUCCESS('✓ Grupo cajero creado'))

        # ── USUARIOS ─────────────────────────────────────────
        usuarios = [
            ('admin',   'admin1234',   True,  [admin_group]),
            ('mesero',  'mesero1234',  False, [mesero_group]),
            ('cajero',  'cajero1234',  False, [cajero_group]),
        ]

        for username, password, is_staff, groups in usuarios:
            user, created = User.objects.get_or_create(username=username)
            user.set_password(password)
            user.is_staff = is_staff
            user.is_superuser = False
            user.save()
            user.groups.set(groups)
            estado = 'creado' if created else 'actualizado'
            self.stdout.write(self.style.SUCCESS(f'✓ Usuario "{username}" {estado}'))

        self.stdout.write(self.style.SUCCESS('\n✅ Roles y usuarios listos'))