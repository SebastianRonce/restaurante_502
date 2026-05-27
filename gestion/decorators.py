from django.shortcuts import redirect


def rol_requerido(*roles):
    """
    Uso: @rol_requerido('administrador')
         @rol_requerido('mesero', 'administrador')
    """
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            grupos = request.user.groups.values_list('name', flat=True)
            if any(r in grupos for r in roles):
                return view_func(request, *args, **kwargs)
            return redirect('acceso_denegado')
        wrapper.__name__ = view_func.__name__
        return wrapper
    return decorator
