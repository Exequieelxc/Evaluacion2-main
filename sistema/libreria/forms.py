from django import forms
from .models import Libro
from .models import Proveedor

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'