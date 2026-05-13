from django import forms

from .models import (
    Cliente,
    Empleado,
    Mesa,
    Plato,
    Orden,
    Factura
)


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'


class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = '__all__'


class MesaForm(forms.ModelForm):

    class Meta:
        model = Mesa
        fields = '__all__'


class PlatoForm(forms.ModelForm):

    class Meta:
        model = Plato
        fields = '__all__'


class OrdenForm(forms.ModelForm):

    class Meta:
        model = Orden
        exclude = ['total']


class FacturaForm(forms.ModelForm):

    class Meta:
        model = Factura

        exclude = [
            'subtotal',
            'impuesto',
            'total_factura'
        ]