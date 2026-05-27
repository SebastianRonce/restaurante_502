from django import forms
from django.forms import inlineformset_factory
from django.core import validators

from .models import Cliente, Empleado, Mesa, Plato, Orden, Factura, DetalleOrden

solo_numeros = validators.RegexValidator(
    regex=r'^\d+$',
    message='El teléfono solo debe contener números.'
)


class ClienteForm(forms.ModelForm):
    telefono = forms.CharField(validators=[solo_numeros])
    class Meta:
        model = Cliente
        fields = '__all__'


class EmpleadoForm(forms.ModelForm):
    telefono = forms.CharField(validators=[solo_numeros])
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
        fields = ['cliente', 'empleado', 'mesa', 'estado_orden']


class DetalleOrdenForm(forms.ModelForm):
    class Meta:
        model = DetalleOrden
        fields = ['plato', 'cantidad']
        widgets = {
            'cantidad': forms.NumberInput(attrs={'min': 1, 'value': 1}),
        }


DetalleOrdenFormSet = inlineformset_factory(
    Orden,
    DetalleOrden,
    form=DetalleOrdenForm,
    extra=1,
    can_delete=True,
    min_num=1,
    validate_min=True,
)


class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        exclude = ['subtotal', 'impuesto', 'total_factura']
