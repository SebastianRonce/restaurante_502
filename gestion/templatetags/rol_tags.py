from django import template

register = template.Library()

@register.filter
def tiene_rol(user, roles_str):
    """
    Uso: {{ user|tiene_rol:"administrador,mesero" }}
    Retorna True si el usuario pertenece a alguno de los roles indicados.
    """
    if not user.is_authenticated:
        return False
    roles = [r.strip() for r in roles_str.split(',')]
    grupos = user.groups.values_list('name', flat=True)
    return any(r in grupos for r in roles)
